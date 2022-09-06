
from .celery import app
from .heartbeat.daemon import Daemon


@app.task
def daemon_publisher(**kwargs):
    print(kwargs)


# Daemon instance
daemon = Daemon(name="hello-world", publisher=daemon_publisher)
daemon.broadcast()


@app.task
def worker(name: str) -> str:
    return f"Hello, {name or 'world'}!"
