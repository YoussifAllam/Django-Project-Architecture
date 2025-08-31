# Use the Python executable to run commands
PYTHON = python3

# Default target to avoid issues with no target specified
.DEFAULT_GOAL := help

# Help text for targets
help:
	@echo "Available commands:"
	@echo "run         - Run the development server"
	@echo "mi    	   - Apply database migrations"
	@echo "make        - Create new migrations"
	@echo "shell       - Open the Django shell"
	@echo "test        - Run tests"
	@echo "superuser   - Create a superuser"
	@echo "clean       - Remove __pycache__ and *.pyc files"
	@echo "clean-migrations - Delete all migration files except __init__.py"
	@echo "static      - Collect static files"

# Django commands
run:
	$(PYTHON) manage.py runserver

mi:
	$(PYTHON) manage.py migrate

make:
	$(PYTHON) manage.py makemigrations

shell:
	$(PYTHON) manage.py shell

test:
	$(PYTHON) manage.py test

superuser:
	$(PYTHON) manage.py createsuperuser

static:
	$(PYTHON) manage.py collectstatic

# Utility command
clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
