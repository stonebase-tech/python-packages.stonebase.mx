import os

from rhdzmota.version import Version


version = Version.from_path(
    name="{{cookiecutter.project_slug}}_version",
    dirpath=os.path.dirname(__file__),
)
