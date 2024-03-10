# package.rhdzmota.com

My personal python package that contains general tooling for software, data engineering, and machine learning projects. 

## RHDZMOTA Python Package

This package is available at PyPI! Check it out [here](https://pypi.org/project/rhdzmota/).

The `rhdzmota` is designed to be a modular toolbox. The main package (i.e., `rhdzmota`) will try to avoid any large third-party dependencies and only focus on develop lightweight core tooling. 

Option 1: Installation of the core package on `standalone` version.

```commanline
$ pip install 'rhdzmota[standalone]'
```

Option 2: Installation of the core package with an extension (at least one).

```commandline
$ pip install 'rhdzmota[ext.hello_world]'
```
* General pattern: `'rhzmota[ext.{{extension_slug}}]'`

The extension source code can be found in the `extension/` directory at the root of this repositry. Each sub-directory placed on the first level within the `extension/` path an standalone python package that's linked to the main `rhdzmota` package as an "extras" dependency.

Both the main `rhdzmota` and extension packages share a common namespace: `rhdzmota`. This means that imports will always share the same prefix. For extensions, an additional namespace is added: `rhdzmota.ext`

**Example 1**: Importing the `Env` enum from the `settings` module on the core package.

```python
from rhdzmota.settings import Env

...
```

**Example 2**: Importing the `hello` function from the `functions` module from the `hello_world` extension. 

```python
from rhdzmota.ext.hello_world.functions import hello

...
```

## Understanding Dependency Tags

The `rhdzmota` package is designed to be composable. This means that you can extend functionality by
installing package extensions.

As demonstrated before, you can install one or more package extensions with the dependency-extras notation. Example:

```commandline
$ pip install 'rhdzmota[ext.hello_world,ext.streamlit_webapps]'
```

An standalone version of the `rhdzmota` package is provided via the `standalone` dependency tag. Although, please consider that this version is not designed to be compliant with the extensions (e.g., the main package installs the `sentry` dependency on the standalone version, but uses `sentry-tornado` when installed with the `ext.streamlit_webapps` tag instead).

The `standalone` tag, taggs all the dependencies that should be installed to use the `rhdzmota` package without any extension. Each package extension can basically do one of the following:
* Add new dependencies only required by the extension. For example, the `ext.streamlit_webapps` adds `streamlit` dependency.
* Drop or replace dependencies from the standalone version: For example, the `ext.streamlit_webapps` replaced the `sentry` dependency with a `sentry-tornado` dependency that allows us better monitoring of the streamlit backend.

As a result, once we identify tag the dependencies required for the standalone execution, we can define the following tags:
* `baseline` tag: is a subset of the standalone dependency set that contains all the dependencies that were not dropped/replaced by any extension.
* `all` tag:  contains a complete set of dependencies.

