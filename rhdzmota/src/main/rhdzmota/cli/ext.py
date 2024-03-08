import importlib
from dataclasses import dataclass
from typing import Callable, Optional

from rhdzmota.interface.cli import CLIBase


@dataclass(slots=True)
class CLIExt(CLIBase):
    overwrite_module_name_cli: Optional[str] = None
    overwrite_namespace: Optional[str] = None

    @classmethod
    def defaults(cls):
        return cls()

    def __post_init__(self):
        # Defaults
        self.module_name_cli = self.overwrite_module_name_cli or "cli"
        self.namespace = self.overwrite_namespace or "rhdzmota.ext"
        # Define import patterns
        super(CLIExt, self).__init__()

    def get_import_pattern(self, extension: str) -> str:
        return ".".join(
            [
                self.namespace,
                extension,
                self.module_name_cli,
            ]
        )

    def get_extension_module(self, extension: str):
        return importlib.import_module(self.get_import_pattern(extension=extension))

    def execute(self, extension: str, command: str, *args, **kwargs):
        extension_module = self.get_extension_module(extension=extension)
        ext_cli = getattr(extension_module, "CLI")
        with ext_cli(
            extension_import_pattern=self.get_import_pattern(extension),
        ) as cli:
            cmd = getattr(cli, command)
            if not isinstance(cmd, Callable):
                return cmd
            return cmd(*args, **kwargs)


def ext():
    import fire

    with CLIExt.defaults() as cli:
        fire.Fire(cli)
