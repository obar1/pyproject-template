# pyproject-template

simple pyproject template with some factories and potery and linters

### Installation

* Install Poetry: <https://python-poetry.org/docs/#installation>
* Install python env: `pyenv install 3.7.0`
* Install virtual env: `pyenv virtualenv 3.7.0 py37pyproject`
* Activate virtual env: `pyenv activate py37`
* Install package and dependencies: `poetry install`
* Install pre-commit hooks: `poetry run pre-commit install`

### Run pre-commit hooks manually

All pre-commit hooks will be run automatically when pushing changes.
They can also be run on staged files or on all files manually:

```bash
# Run all hooks against currently staged files,
# this is what pre-commit runs by default when committing:
pre-commit run

# Run all the hooks against all the files:
pre-commit run --all-files

# Run a specific hook against all staged files:
pre-commit run black
pre-commit run flake8
pre-commit run isort
pre-commit run pylint
```

### Continuous pytest

```bash
export PYTHONPATH=. && ptw -c  -- --capture=tee-sys -o log_cli=true
```

## Sample usage
> I added some simple functionality just to make this doing something :P

```bash
mkdir repo
cp tests/resources/repo/map.yaml repo
export CONFIG_FILE='./repo/map.yaml'
python main.py help

python main.py create_section  'https://www.github.com'

```