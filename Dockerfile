FROM python:3.11
ENV POETRY_VERSION=1.5.1
RUN pip install "poetry==$POETRY_VERSION"
WORKDIR /hbot
COPY poetry.lock pyproject.toml /hbot/
RUN poetry install --no-interaction --no-ansi
COPY . /hbot/
CMD poetry run python index.py