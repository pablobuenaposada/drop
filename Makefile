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

run: venv
	PYTHONPATH=src venv/bin/python src/main.py --file=$(file)

docker/build:
	docker build --no-cache	--tag=curry .

docker/run:
	docker run -e file=$(file) --rm -it -v $(shell pwd)/$(file):/usr/src/app/$(file) curry

docker/tests:
	 docker run curry /bin/sh -c 'make tests'