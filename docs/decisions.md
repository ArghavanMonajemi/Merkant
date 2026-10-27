# Technical decisions

| Decision | Why | Status |
|---|---|---|
| uv for dependencies | One lock file, fast, reproducible builds | Decided |
| Multi-stage Dockerfile (dev, prod) | Staging runs the same image as production | Decided |
| PostgreSQL in staging and production, SQLite in development | Simple local setup, real database where it matters | Decided |
| Single settings.py with an ENVIRONMENT switch | Small project, one file is enough for now | Decided |
| Celery + Redis for background work | Emails must not block requests | Decided |
| drf-spectacular for OpenAPI docs | OpenAPI 3 and actively maintained | Decided |
| pytest + pytest-django | Plain asserts and fixtures | Decided |
| One error format for every response | Frontend can handle all errors the same way | Decided |
| Authentication type (JWT or token) | | Open |
| Translation approach for multilingual models | | Open |
| Where Address lives (account or order) | | Open |
| Category tree (package or parent field) | | Open |
| User types (roles on one User model, or separate models) | | Open |