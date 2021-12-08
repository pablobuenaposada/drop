venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

format/isort: venv
	venv/bin/isort src

format/black: venv
	venv/bin/black --verbose src

format: venv format/isort format/black

tests: venv
	PYTHONPATH=src venv/bin/pytest src/tests
