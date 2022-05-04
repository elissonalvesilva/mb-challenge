import requests

if __name__ == "__main__":
    cont = True
    while cont:
        try:
            response = requests.get('http://localhost:3000/v4/BRLBTC/candles?from=1&to=2')
            print(response.status_code)
            if response.status_code < 300:
                cont = False
        except Exception as e:
            print(e)
            cont = True
