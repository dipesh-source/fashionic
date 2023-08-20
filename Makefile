.PHONY: run

run:
	@echo "Starting Django server..."
	pipenv run python manage.py runserver

run-celery:
	@echo "Starting Celery worker and beat in the background..."
	pipenv run celery -A fashionic worker --loglevel=info & pipenv run celery -A fashionic beat --loglevel=info

mg:
	@echo "Starting makemigrations files..."
	pipenv run python manage.py makemigrations

mr:
	@echo "Starting migrate files..."
	pipenv run python manage.py migrate

load:
	@echo "Starting generating fixtures files..."
	pipenv run python fixtures.py

loaddata:
	@echo "Starting loading fixtures to database..."
	pipenv run python manage.py loaddata fixtures/service.json
	pipenv run python manage.py loaddata fixtures/staff.json
	pipenv run python manage.py loaddata fixtures/feedback.json
	pipenv run python manage.py loaddata fixtures/product.json
	pipenv run python manage.py loaddata fixtures/gallery.json
	pipenv run python manage.py loaddata fixtures/purchase.json
	pipenv run python manage.py loaddata fixtures/attendance.json
	pipenv run python manage.py loaddata fixtures/appointment.json
