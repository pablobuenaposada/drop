# Curry wholesaler

## Usage with Docker
Step in project folder: 
```bash
cd drop/
```
Build docker image with:
```bash
make docker/build
```

### Run the solver
do:
```bash
make docker/run file=example.txt
```
would output something like:
```bash
docker run -e file=example.txt --rm -it -v /Users/pablobuenaposadasanchez/Desktop/drop/example.txt:/usr/src/app/example.txt curry
PYTHONPATH=src venv/bin/python src/main.py --file=example.txt
V M V M V
```

### Run tests
```bash
make docker/test
```
output:
```bash
pablo@MacBook-Pro drop % make docker/tests
docker run curry /bin/sh -c 'make tests'
PYTHONPATH=src venv/bin/pytest src/tests
============================= test session starts ==============================
platform linux -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /usr/src/app
collected 21 items

src/tests/test_main.py ........                                          [ 38%]
src/tests/test_models.py .............                                   [100%]

============================== 21 passed in 1.37s ==============================
```

## Usage without Docker
Step in project folder:
```bash
cd drop/
```
### Run the solver
Make sure that the command `python3 --version` in your local outputs this:
```bash
Python 3.9.7
```
Then you can just do:
```bash
make run file=example.txt
```
output:
```bash
pablo@MacBook-Pro drop % make run file=example.txt
python3 -m venv venv
venv/bin/pip install -r requirements.txt
Collecting pytest
  Using cached pytest-6.2.5-py3-none-any.whl (280 kB)
...
Installing collected packages: pyparsing, typing-extensions, tomli, toml, py, pluggy, platformdirs, pathspec, packaging, mypy-extensions, iniconfig, click, attrs, pytest, isort, black
Successfully installed attrs-21.2.0 black-21.12b0 click-8.0.3 iniconfig-1.1.1 isort-5.10.1 mypy-extensions-0.4.3 packaging-21.3 pathspec-0.9.0 platformdirs-2.4.0 pluggy-1.0.0 py-1.11.0 pyparsing-3.0.6 pytest-6.2.5 toml-0.10.2 tomli-1.2.2 typing-extensions-4.0.1
PYTHONPATH=src venv/bin/python src/main.py --file=example.txt
V M V M V
```

### Run tests
```bash
make test
```
output:
```bash
PYTHONPATH=src venv/bin/pytest src/tests
================================================================================== test session starts ===================================================================================
platform darwin -- Python 3.9.7, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/pablobuenaposadasanchez/Desktop/drop
collected 21 items

src/tests/test_main.py ........                                                                                                                                                    [ 38%]
src/tests/test_models.py .............                                                                                                                                             [100%]

=================================================================================== 21 passed in 2.82s ===================================================================================
```
