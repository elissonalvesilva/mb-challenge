build:
	docker-compose build

up:
	docker-compose up -d

logs-api:
	docker logs --follow --timestamps mms_api

logs-fake-api:
	docker logs --follow --timestamps fakeapi

generate-data:
	docker-compose run script python app/ingestion.py

retry:
	docker-compose run script python app/retry.py

check-unprocessed-days:
	docker-compose run script python app/check_unprocessed_days.py

test-api:
	docker-compose run mms_api python -m pytest -v
