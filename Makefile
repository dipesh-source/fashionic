.PHONY: run

run:
	pipenv run python manage.py runserver

mg:
	pipenv run python manage.py makemigrations

mr:
	pipenv run python manage.py migrate
