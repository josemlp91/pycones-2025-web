FROM python:3.13-slim

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV PORT=8000
EXPOSE $PORT


# Install node via instructions at https://github.com/nodesource/distributions
RUN apt-get update \
    && apt-get install --no-install-recommends -qy git curl bash ca-certificates gnupg libxml2-dev libxslt-dev build-essential unzip

RUN curl -fsSL https://bun.sh/install | bash
RUN apt clean && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY uv.lock pyproject.toml /app/
RUN uv sync --frozen --no-cache --no-dev


CMD ["uv", "run", "python","-m", "pelican", "-lr", "/app/content", "-o", "/app/output", "-s", "/app/pelicanconf.py", "-p", "8000", "-b", "0.0.0.0"]
