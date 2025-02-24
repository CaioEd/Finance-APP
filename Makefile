update-requirements:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

database:
	docker compose up -d

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver
