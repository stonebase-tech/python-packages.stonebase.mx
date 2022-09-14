celery -A rhdzmota.celery worker --loglevel=INFO --concurrency=1 -O fair -P prefork -Q queue_heartbeat
