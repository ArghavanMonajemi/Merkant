import tempfile
from decouple import config
from .settings import *

# Database: SQLite in memory by default, Postgres when asked (used in CI)
if config("USE_POSTGRES_FOR_TESTS", default=False, cast=bool):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("POSTGRES_DB"),
            "USER": config("POSTGRES_USER"),
            "PASSWORD": config("POSTGRES_PASSWORD"),
            "HOST": config("POSTGRES_HOST", default="localhost"),
            "PORT": config("POSTGRES_PORT", default=5432, cast=int),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",
        }
    }

# Faster password hashing
PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

# Emails go to memory, not the network
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# Celery tasks run immediately, no Redis needed
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# Uploaded files go to a temporary folder
MEDIA_ROOT = tempfile.mkdtemp()

# No rate limiting in tests
REST_FRAMEWORK = {**REST_FRAMEWORK, "DEFAULT_THROTTLE_CLASSES": []}