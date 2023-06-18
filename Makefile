.PHONY: run

run:
	pipenv run python manage.py runserver

mg:
	pipenv run python manage.py makemigrations

mr:
	pipenv run python manage.py migrate

load:
	pipenv run python fixtures.py

loaddata:
	pipenv run python manage.py loaddata fixtures/service.json
	pipenv run python manage.py loaddata fixtures/staff.json
	pipenv run python manage.py loaddata fixtures/feedback.json
	pipenv run python manage.py loaddata fixtures/product.json
	pipenv run python manage.py loaddata fixtures/gallery.json
	pipenv run python manage.py loaddata fixtures/purchase.json
	pipenv run python manage.py loaddata fixtures/attendance.json
	pipenv run python manage.py loaddata fixtures/appointment.json
