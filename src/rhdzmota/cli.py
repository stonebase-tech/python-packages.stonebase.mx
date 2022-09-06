import time
from typing import Optional

from .settings import logger_manager
from .interface.cli import CLIBase
from .utils.gists import Gist


logger = logger_manager.get_logger(name=__name__)


class CLI(CLIBase):

    @CLIBase.Formatter(default=str)
    def hello(self, world: Optional[str] = None, sleep: int = 1, delegate: bool = False):
        from .celery_worker_hello import worker

        world = world or "world"
        time.sleep(sleep)

        if delegate:
            return worker.delay(name=world)

        logger.debug("CLI Hello command execution.")
        return worker(name=world)

    @CLIBase.Formatter()
    def gist(
            self,
            username: str,
            gist_id: str,
            filename: str,
            commit: Optional[str] = None,
            save: bool = False
    ):
        # Retrieve code
        code = Gist(username=username, gist_id=gist_id, filename=filename, commit=commit).get_code()
        # Save code into a file when requested
        if save:
            with open(filename, "w") as file:
                file.write(code)
        return f"\n\n{code}"
