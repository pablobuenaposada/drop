FROM python:3.9.7

WORKDIR /usr/src/app

COPY src /usr/src/app/src
COPY Makefile requirements.txt /usr/src/app/

RUN make venv

CMD ["make", "run"]