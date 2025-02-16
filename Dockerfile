FROM python:3.13-slim

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV PORT=8000
EXPOSE $PORT


# Install node via instructions at https://github.com/nodesource/distributions
RUN apt-get update \
    && apt-get install --no-install-recommends -qy git curl bash ca-certificates gnupg libxml2-dev libxslt-dev build-essential

RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt install -y nodejs \
    && apt clean && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv ~/.local/bin/uv /usr/local/bin/uv

WORKDIR /app

COPY uv.lock pyproject.toml /app/
RUN uv sync --frozen --no-cache --no-dev

RUN uv pip list | grep pelican


CMD ["uv", "run", "python","-m", "pelican", "-lr", "/app/content", "-o", "/app/output", "-s", "/app/pelicanconf.py", "-p", "8000", "-b", "0.0.0.0"]
