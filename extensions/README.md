# RHDZMOTA Extension Packages

```commandline
$ pip install 'rhdzmota[<ext-name>]'
```

## Local Installation

**Linked installation**: you can install your extension indirectly by specifying an `extras` tag when installing the main `rhdzmota` package. For example:

```commandline
$ pip install 'rhdzmota[ext.hello_world]'
```
* General pattern: `rhdzmota[ext.<extension-name>]`

**Standalone installation**: if your extension is not yet linked to the main package, you can proceed
with an standaline installation. For this installation type, you only need to run `pip install -e` over your extension: 

```commandline
$ EXT_BUILD_LOCAL=1 pip install -e extensions/<ext-package>
```
* It is recommended (but not required) to have `rhdzmota` installed beforehand.
