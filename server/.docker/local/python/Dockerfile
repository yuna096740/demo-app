FROM python:3.11

WORKDIR /app/

ENV POETRY_HOME=/opt/poetry
ENV PATH="$POETRY_HOME/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN curl -sSL https://install.python-poetry.org | python -

COPY pyproject.toml* poetry.lock* /app/

RUN poetry config virtualenvs.in-project true

RUN poetry install --no-root

COPY app /app/app