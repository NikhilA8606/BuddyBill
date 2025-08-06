FROM python:3.13-slim-bookworm

ARG APP_HOME=/app

WORKDIR $APP_HOME

ENV PIPENV_CACHE_DIR=/root/.cache/pip

RUN apt-get update && apt-get install --no-install-recommends -y \
  build-essential libjpeg-dev zlib1g-dev libgmp-dev \
  libpq-dev gettext wget curl gnupg git \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

ENV PATH=/.venv/bin:$PATH
RUN python -m venv /.venv
RUN --mount=type=cache,target=/root/.cache/pip pip install pipenv==2023.12.1

COPY Pipfile Pipfile.lock $APP_HOME/
RUN --mount=type=cache,target=/root/.cache/pip pipenv  install --system --categories "packages"

COPY docker $APP_HOME/


