# Environment setup

## Requirements
- Docker with Compose
- uv (for local editing and IDE support)

## First run (development)
```bash
uv sync                                  # creates .venv for your IDE
cp .env.example .env                     # then fill in the values
docker compose -f docker-compose-development.yml up --build
```
API: http://localhost:8000, docs: http://localhost:8000/api/docs/

## Common commands
```bash
# migrations
docker compose -f docker-compose-development.yml exec backend python manage.py migrate

# add a package
uv add package-name        # then rebuild with up --build

# run tests (from src/merkant)
uv run pytest
```

## Environment variables

| Variable | Meaning |
|---|---|
| ENVIRONMENT | development, staging or production |
| SECRET_KEY | Django secret key (unique per stage) |
| DEBUG | True only in development |
| ALLOWED_HOSTS | Comma-separated hostnames |
| POSTGRES_DB / USER / PASSWORD | Database credentials (staging and production) |
| POSTGRES_HOST / POSTGRES_PORT | Database address (`db` and `5432` in Docker) |
| USE_POSTGRES_FOR_TESTS | True in CI, so tests run on PostgreSQL |
| EMAIL_BACKEND / HOST / PORT | Where Django sends mail (smtp4dev in development) |
| EMAIL_USE_TLS / EMAIL_USE_SSL | Encryption for the mail server, never both True |
| EMAIL_HOST_USER / PASSWORD | Mail server login (empty in development) |
| DEFAULT_FROM_EMAIL | Sender address on outgoing mail |
| CELERY_BROKER_URL | Where tasks are queued (Redis database 0) |
| CELERY_RESULT_BACKEND | Where task results are stored (Redis database 1) |

Never commit `.env`, `.env.stage` or `.env.prod`. Commit only `.env.example`.

## Staging and production
Use the compose file for the stage together with its env file. See `docker-compose-*.yml`.