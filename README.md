# package.rhdzmota.com

My personal python package that contains general tooling for software, data engineering, and machine learning projects. 

## RHDZMOTA Python Package

This package is available at PyPI! Check it out [here](https://pypi.org/project/rhdzmota/).

The `rhdzmota` is designed to be a modular toolbox. The main package (i.e., `rhdzmota`) will try to avoid any large third-party dependencies and only focus on develop lightweight core tooling. 

Installation of the core package:

```commanline
$ pip install rhdzmota
```

Installation of the core package with an extension:

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

