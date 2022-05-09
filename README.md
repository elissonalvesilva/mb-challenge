# Mercado Bitcoin Challenge

## Tecnologias
 - Python = 3.8
 - Pytest
 - Pymongo
 - Mongodb
 - Pandas
 - Flask

## Setup
Basta rodar os comandos abaixo:
> make build

> make up

**Obs: esse comando serve para subir a aplicação da api e da api fake que o script consome os dados. Tive que criar uma api fake devido nao consegui fazer requests locais para api do candles**

## Logs:
Logs da api:
> make logs-api

Logs da apifake:
> make logs-fake-api

## Test
> make test-api

## Script 
O script em si é divido em tres scripts

### 1 - ingestion.py
> Responsavel por fazer a ingestão de dados da API do MB(ness caso aqui é a fakeapi), calcular os MMS e salvar no mongodb. Caso falhe a request devido a indisponibilidade ele salva um arquivo as urls que devem ser reprocessadas e o proximo script vai ser responsavel de ler esse arquivo e reprocessar enviando um comando para esse script com os parametros.

Como rodar para um caso de teste:
> make generate-data

caso queira rodar ele corretamente:
> python app/ingestion.py -sd 2021-05-05

**Obs: a ideia desse script ele dele rodar de todo final de dia as 23:00 utilizando um agendador de job ou con cron ou qualquer outra tecnologia**

Parametros:

parametro | valor | descrição
---------| ------| ---------
-sd ou --start-date | inteiro (timestamp) | data de inicio para ingestao de dados. 
-ed ou --end-date | inteiro (timestamp) | data de fim para ingestao de dados. Default: dia anterior
-r ou --retry | bool | indica que o script ocorrera em forma de retry
-pr ou --pairs-retry | list de string | indica quais pairs voce quer rodar para o script para retry. Deve ser separado por ','. Exemplo: PAIR1, PAIR2


### 2 - retry.py
> Responsavel por ler o arquivo de retries e executar novamente o script de ingestao

Execução:
> make retry

**Obs: ele somente é executado de forma manual. Mas se quiser deixar de forma automatica podemos deixar ele rodando em um cron de 12 em 12 hrs**

#### check_unprocessed_days.py
> Responsavel por checar se possuem dias que nao forma processado os MMS no banco de dados. Caso exista ele escreve em um arquivo os dias nao processados.

Execução:
> make check-unprocessed-days

### Ideias dos scripts
Os scripts em si foram criados para salvar os dados em arquivo como forma de facilitar mais o projeto e a compreensão. Mas caso houvesse a possibilidade de scala poderiam ser facilmente enviados para uma fila onde conteriam microseriços de avisos (no caso tivesses dados com datas nao processadas no banco ou também avisando que falhou uma ingestao de data no dia)

Alem disso, o script de ingestao foi criado utilizando a ideia de threads com o proposito principal de processar uma grande quantidade de dados.


### Estrutura script
```
 - app
    - config/ -> carregamento do arquivo de configuração e envs
    - database -> responsavel por fazer o load dos dados no DB
    - job_definitions -> definições dos jobs que serao rodados (pairs, ranges, tables, actions)
    - shared 
      - args_parser -> responsavel por parseamentos dos args do command line
      - execution_info -> responsavel por criar um log mais bonito
      - file_manager -> responsavel por criar, escrever, etc em arquivos
      - formmater -> formatador da resposta para enviar para o calculo de MMS
      - Job -> classes de execução
      - job_loader -> responsavel por ler o arquivo de definition e gerar jobs para serem executados
      - jobs_manager -> responsavel por orquestrar toda execuçao de jobs em threads
      - output_formatter -> responsavel por formatar os dados pra ser salvos no DB
      - process_data -> responsael por calcular os MMS para cada job
      - request -> responsavel por fazer request para api
      - Singleton -> classes decorator
      - system_configure -> responsavel por criar toda configuração do script ao iniciar
      - system_exiter -> responsavel por encerrar o script em caso de falhar com messagem
      - writer -> responsavel por salvar dados em arquivo

    - check_unprocessed_days.py -> script responsavel por checkar inconsistencia de dados nao processados no banco
    - ingestion.py -> script responsavel por fazer ingestao de dados
    - retry -> script responsaevl por ler o arquivo de retry e executar noamente a ingestao para os pair que falharam 

```
