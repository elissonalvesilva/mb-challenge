generate-data:
	docker-compose run script python app/ingestion.py

retry:
	docker-compose run script python app/retry.py

check-unprocessed-days:
	docker-compose run script python app/check_unprocessed_days.py
