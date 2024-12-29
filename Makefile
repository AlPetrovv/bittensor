DC = docker compose
EXEC = docker exec -it
MANAGE_PY = python manage.py

APP_CONTAINER = bittensor-django
POSTGRES_CONTAINER = bittensor-db
APP_CONTAINER_DEV = bittensor-django-dev
POSTGRES_CONTAINER_DEV = bittensor-db-dev

APP_SERVICE = django
POSTGRES_SERVICE = postgres

DOCKER_COMPOSE_FILE = docker_compose/docker-compose.yaml
DOCKER_COMPOSE_DEV_FILE = docker_compose/docker-compose.dev.yaml
ENV = --env-file=docker_compose/envs/dc_file.env
DEV_ENV = --env-file=docker_compose/envs/dc_file.dev.env


.PHONY: update-prod
update-prod: git-pull build run

.PHONY: git-pull
git-pull:
	git pull

.PHONY: run
run: stop
	${DC} -f ${DOCKER_COMPOSE_FILE} ${ENV} up -d

.PHONY: build
build:
	${DC} -f ${DOCKER_COMPOSE_FILE} ${ENV} build

.PHONY: stop
stop:
	${DC} -f ${DOCKER_COMPOSE_FILE} ${ENV} down

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate

.PHONY: migrations
migrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations

.PHONY: create-superuser
create-superuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

# Dev
.PHONY: dev-run
dev-run: dev-stop
	${DC} -f ${DOCKER_COMPOSE_DEV_FILE} ${DEV_ENV} up  --build

.PHONY: dev-stop
dev-stop:
	${DC} -f ${DOCKER_COMPOSE_DEV_FILE} ${DEV_ENV} down

.PHONY: dev-run-app
dev-run-app:
	${DC} -f ${DOCKER_COMPOSE_DEV_FILE} ${DEV_ENV} up --build ${APP_SERVICE}

dev-run-db: dev-stop-db
	${DC} -f ${DOCKER_COMPOSE_DEV_FILE} ${DEV_ENV} up  ${POSTGRES_SERVICE}

dev-stop-db:
	${DC} -f ${DOCKER_COMPOSE_DEV_FILE} ${DEV_ENV} down ${POSTGRES_SERVICE}

dev-migrate:
	${EXEC} ${APP_CONTAINER_DEV} ${MANAGE_PY} migrate

dev-migrations:
	${EXEC} ${APP_CONTAINER_DEV} ${MANAGE_PY} makemigrations

dev-create-superuser:
	${EXEC} ${APP_CONTAINER_DEV} ${MANAGE_PY} createsuperuser

