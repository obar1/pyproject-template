venv0:
	virtualenv venv
	@echo "$  . ./venv/bin/activate"

jupyter0:
	 . ./venv/bin/activate

install:
	pip install --upgrade pip && pip install -r requirements.txt
	pre-commit install

test:
	python -m pytest -x pyproject-template/tests/test_*.py
	python -m pytest -x -vv --nbval-lax *.ipynb

format:
	black pyproject-template

lint:
	pylint --disable=R,C,W0702,W0621,W1203 pyproject-template

refactor: format lint
