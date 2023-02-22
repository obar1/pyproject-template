venv0:
	virtualenv venv
	echo "$  . venv/bin/activate"

install:
	pip install --upgrade pip && pip install -r requirements.txt
	pre-commit install

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:
	black .

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

refactor: format lint

deploy:
	echo "TODO: deploy"

all: install lint test format deploy
