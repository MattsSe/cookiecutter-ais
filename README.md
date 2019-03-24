Python AIS Project Template
===========================

[![Travis CI build status](https://travis-ci.org/MattsSe/cookiecutter-ais.png?branch=master)](%60travis%60_)

This is a [Cookiecutter](http://cookiecutter.readthedocs.org) template
for creating a Python application project.

The project layout is based on the [Python Packaging User
Guide](https://packaging.python.org/en/latest/distributing.html#configuring-your-project).
The current conventional wisdom forgoes the use of a source directory,
but moving the package out of the project root provides several
advantages (*cf.* [Packaging a Python
library](http://blog.ionelmc.ro/2014/05/25/python-packaging)).

Template Project Features
=========================

-   Python 3.5+
-   [pytest](http://pytest.org) test suite
-   [Sphinx](http://sphinx-doc.org) documentation

Template Application Features
=============================

-   CLI with subcommands
-   Logging
-   Hierarchical [YAML](http://pyyaml.org/wiki/PyYAML) configuration

Usage
=====

Assuming conda is installed

Install [cookiecutter](https://github.com/audreyr/cookiecutter) template cli 

```bash
$ pip install cookiecutter
```

Create a new project directly from the template on
[Gitlab](https://gitlab.lrz.de/ga63hav/cookiecutter-ais):

```bash
$ cookiecutter git+https://gitlab.lrz.de/ga63hav/cookiecutter-ais
```

Create a new python project the cookiecutter-ais template. Run the
cookiecutter generator and set your configs interactively in the
console.

```bash
cookiecutter git+https://gitlab.lrz.de/ga63hav/cookiecutter-ais
# enter the configs in the interactive shell
cd <the-given-app-name>
```

Create a new conda environment for this project

```bash
conda env create -f environment.yml
```

Or install Python requirements for using the template:

```bash
python -m pip install --requirement=requirements.txt --user
```
