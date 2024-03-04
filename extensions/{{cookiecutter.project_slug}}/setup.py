import os
from setuptools import setup, find_namespace_packages

# Environ variables
EXT_CODEBASE_PATH = os.environ.get(
    "EXT_CODEBASE_PATH",
    default=os.path.join("src", "main")
)
EXT_BUILD_LOCAL = int(os.environ.get(
    "EXT_BUILD_LOCAL",
    default="0",
))

with open("README.md", "r") as file:
    readme = file.read()

with open("requirements.txt", "r") as file:
    requirements = [
        req.strip()
        for req in file.read().splitlines()
        if req and not req.startswith("#")
    ]
    # If local build, do not install `rhdzmota` from pypi
    requirements.pop(requirements.index("rhdzmota"))

version_filename = "{{cookiecutter.project_slug}}_version"
version_filepath = os.path.join(
    EXT_CODEBASE_PATH,
    "rhdzmota",
    "ext",
    version_filename,
)

with open(version_filepath, "r") as file:
    version = file.readline().strip()

setup(
    name="rhdzmota_extension_{{cookiecutter.project_slug}}",
    version=version,
    description=(
        "RHDZMOTA Extension App: {{cookiecutter.project_slug}}"
    ),
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Rodrigo H. Mota",
    author_email="info@rhdzmota.com",
    url="https://github.com/rhdzmota/package.rhdzmota.com",
    classifiers=[
        "Typing :: Typed",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
    ],
    package_dir={
        "": EXT_CODEBASE_PATH,
    },
    package_data={
        "": [
            os.path.join(
                "rhdzmota",
                "ext",
                "{{cookiecutter.project_slug}}_version",
            ),
        ],
    },
    packages=[
        package
        for package in find_namespace_packages(where=EXT_CODEBASE_PATH)
        if package.startswith("rhdzmota")
    ],
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.10, <4",
    license="TBD",
    zip_safe=False,
)
