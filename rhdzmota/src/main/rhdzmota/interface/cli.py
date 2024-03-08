import json
import time
import datetime as dt
from typing import Optional

from rhdzmota.settings import (
    get_environ_variable,
    logger_manager,
)


logger = logger_manager.get_logger(name=__name__)


class CLIBase:

    class Formatter:

        def __init__(self, cls: Optional = None, default: Optional = None, serialize: bool = None):  # type: ignore
            self.serialize = serialize
            self.serializer = lambda obj: json.dumps(obj, cls=cls, default=default, indent=4)

        def __call__(self, method):
            def wrapper(other, *args, **kwargs):
                output = method(other, *args, **kwargs)
                if not self.serialize:
                    return output
                if not isinstance(output, str):
                    output = self.serializer(output)
                return output
            return wrapper

    def __init__(
            self,
            extension_import_pattern: Optional[str] = None,
    ):
        self.extension_import_pattern = extension_import_pattern
        self.now = dt.datetime.utcnow().isoformat()
        self.start = time.perf_counter()
        self.end = None

    def now(self, local: bool = False) -> str:
        return (dt.datetime.utcnow() if not local else dt.datetime.now()).isoformat()

    def on_start(self):
        logger.info("CLI Method not implemented: on_start")

    def on_finalize(self):
        logger.info("CLI method not implemented: on_finalize")

    def __enter__(self) -> 'CLIBase':
        self.on_start()
        return self

    def __exit__(self, *args):
        self.on_finalize()
        self.end = time.perf_counter()
        logger.info(f"Command Start Timestamp: {self.now}")
        logger.info(f"Command Duration: {self.end - self.start}")

    @Formatter()
    def environ(self, name: str) -> Optional[str]:
        return get_environ_variable(
            name=name,
            enforce=False,
        )
