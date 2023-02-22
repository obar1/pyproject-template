venv0:
	virtualenv venv
	echo "$  . venv/bin/activate"

install:
	pip install --upgrade pip && pip install -r requirements.txt
	pre-commit install

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:
	black . pyproject-template

lint:
	pylint --disable=R,C pyproject-template

refactor: format lint

