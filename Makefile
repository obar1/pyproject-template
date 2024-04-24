install:
	pip install --upgrade pip && pip install -r requirements.txt
	mypy --install-types


test:
	python -m pytest lib/tests/test_*.py
	python -m pytest -vv --nbval-lax *.ipynb

format:
	black lib

lint:
	pylint --disable=R,C,W0702,W0621,W1203 lib

refactor: format lint test

jupyter9:
	jupyter notebook
