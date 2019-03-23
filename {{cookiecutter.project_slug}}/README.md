{% set delim = "=" * cookiecutter.app_name|length -%}
{{ delim }}
{{ cookiecutter.app_name }}
{{ delim }}

# This is the {{ cookiecutter.app_name }} application.

## Minimum Requirements

-   [conda](https://www.anaconda.org) (for managing the environment)

## Optional Requirements

-   [pytest](http://pytest.org) (for running the test suite)
-   [Sphinx](http://sphinx-doc.org) (for generating documentation)

## Basic Setup

Assuming conda is installed.

Create a new conda environment for this project. This will create a new
environment with the name declared in the [environment.yml file](./environment.yml).

```bash
conda env create -f environment.yml
```

Generate [sqlalchemy](https://www.sqlalchemy.org/) database schema classes.
This will generate a python file `schema.py` with all the sqlalchemy table classes.
```
 sqlacodegen postgresql://<db_name>:<password>@<host>/<db_name> --outfile src/core/schema.py
```

Run the application:

```bash
python -m {{ cookiecutter.app_name }} --help
```

Run the test suite:

```bash
pytest test/
```

Build documentation:

```bash
sphinx-build -b html doc doc/_build/html
```

Install for the current user:

```bash
python setup.py install --user
```

## Further-Links

-   [conda user
    guide](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
