import os
import time
from typing import Optional

from rhdzmota.settings import logger_manager
from rhdzmota.interface.cli import CLIBase
from rhdzmota.utils.gists import Gist


logger = logger_manager.get_logger(name=__name__)


class CLI(CLIBase):

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

    @CLIBase.Formatter()
    def version(self):
        with open(os.path.join(os.path.dirname(__path__), "VERSION"), "r") as file:
            return file.read()


def main():
    import fire

    with CLI() as cli:
        fire.Fire(cli)
    fire.Fire(CLI())
