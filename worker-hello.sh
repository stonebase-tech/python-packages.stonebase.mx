celery -A rhdzmota.celery_workers.hello worker --loglevel=INFO --concurrency=2 -O fair -P prefork
