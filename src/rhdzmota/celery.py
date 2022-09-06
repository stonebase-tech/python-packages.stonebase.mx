from celery import Celery

from .settings import (
    RHDZMOTA_CELERY_BROKER_HOST
)


# Celery application instance
app = Celery(
    "tasks",
    broker=f"redis://{RHDZMOTA_CELERY_BROKER_HOST}",
)
