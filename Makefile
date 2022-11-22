ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

build:
	docker-compose up --build -d --remove-orphans

up:
	docker-compose up -d

down:
	docker-compose down

show-logs:
	docker-compose logs

makemigrations:
	docker-compose exec app python3 manage.py makemigrations

migrate:
	docker-compose exec app python3 manage.py migrate

superuser:
	docker-compose exec app python3 manage.py createsuperuser

collectstatic:
	docker-compose exec app python3 manage.py collectstatic --no-input --clear

down-v:
	docker-compose down -v

volume:
	docker volume inspect intropixel_postgres_data

db:
	docker-compose exec postgres-db psql --username=root --dbname=intropixel

test:
	docker-compose exec app pytest -p no:warnings --cov=.

test-html:
	docker-compose exec app pytest -p no:warnings --cov=. --cov-report html

flake8:
	docker-compose exec app flake8 .

black-check:
	docker-compose exec app black --check --exclude=migrations .

black-diff:
	docker-compose exec app black --diff --exclude=migrations .

black:
	docker-compose exec app black --exclude=migrations .

isort-check:
	docker-compose exec app isort . --check-only --skip env --skip migrations

isort-diff:
	docker-compose exec app isort . --diff --skip env --skip migrations

isort:
	docker-compose exec app isort . --skip env --skip migrations


