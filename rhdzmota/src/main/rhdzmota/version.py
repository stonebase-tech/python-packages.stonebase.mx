import os
from typing import List, Optional
from dataclasses import dataclass

from rhdzmota.settings import logger_manager


logger = logger_manager.get_logger(name=__name__)


@dataclass(frozen=True, slots=True)
class Version:
    name: str
    value: str
    filepath: Optional[str] = None

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return self.value

    @property
    def components(self) -> List[str]:
        return self.value.split(".")

    @property
    def major(self) -> int:
        component, *_ = self.components
        return int(component)

    @property
    def minor(self) -> int:
        _, component, *_ = self.components
        return int(component)

    @property
    def patch(self) -> int:
        *_, component = self.components
        return int(component)

    @classmethod
    def from_path(cls, dirpath: str, name: str):
        for file in os.listdir(dirpath):
            if file.lower().endswith("version"):
                filepath = os.path.join(dirpath, file)
                break
        else:
            raise ValueError("Version file not found for package name: " + name)

        with open(filepath, "r") as version_file:
            version_value = version_file.readline().strip()  # TODO: Validate version pattern via regex
            return cls(name=name, value=version_value, filepath=filepath)


version = Version.from_path(name="rhdzmota", dirpath=os.path.dirname(__file__))
