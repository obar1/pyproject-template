venv0:
	virtualenv venv
	@echo "$  . ./venv/bin/activate"


install:
	pip install --upgrade pip
	pip install -r requirements.txt
	pre-commit install
	mypy --install-types

test:
	python -m pytest lib/tests/test_*.py
	python -m pytest -vv --nbval-lax *.ipynb

format:
	black lib

lint:
	pylint --disable=R,C,W0702,W0621,W1203 lib

refactor: format lint

jupyter9:
	jupyter notebook
