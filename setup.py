import os
from setuptools import setup

with open("requirements.txt", "r") as file:
    requirements = [line for line in file.read().splitlines() if line]

with open(os.path.join("src", "rhdzmota", "VERSION"), "r") as file:
    version = file.read().strip()

setup(
    name="rhdzmota",
    version=version,
    author="Rodrigo H. Mota",
    author_email="contact@rhdzmota.com",
    package_dir={
        "": "src"
    },
    install_requires=requirements,
    include_package_data=True,
)
