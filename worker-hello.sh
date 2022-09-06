celery -A rhdzmota.celery_worker_hello worker --loglevel=INFO --concurrency=2 -O fair -P prefork
