# ANSI color codes
COLOR_RESET=\033[0m
COLOR_BOLD=\033[1m
COLOR_GREEN=\033[32m
COLOR_YELLOW=\033[33m

help:
	@echo ""
	@echo "  $(COLOR_YELLOW)Available targets:$(COLOR_RESET)"
	@echo ""
	@echo "  $(COLOR_GREEN)upgrade-pip$(COLOR_RESET)		- Upgrade Pip Version"
	@echo "  $(COLOR_GREEN)install$(COLOR_RESET)		- Install Libraries / Dependencies"
	@echo "  $(COLOR_GREEN)freeze$(COLOR_RESET)		- Freeze Libraries / Dependencies"
	@echo "  $(COLOR_GREEN)database$(COLOR_RESET)		- Start PostgreSQL Database"
	@echo "  $(COLOR_GREEN)migrations$(COLOR_RESET)		- Run Database Migrations"
	@echo "  $(COLOR_GREEN)migrate$(COLOR_RESET)		- Apply Database Migrations"
	@echo "  $(COLOR_GREEN)run$(COLOR_RESET)			- Run Django App"
	@echo ""
	@echo "  $(COLOR_YELLOW)Note:$(COLOR_RESET) Use 'make <target>' to execute a specific target."
	@echo ""

freeze:
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
