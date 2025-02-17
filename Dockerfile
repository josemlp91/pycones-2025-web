FROM python:3.13-slim

ENV LC_ALL=C.UTF-8 \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    PORT=8000

EXPOSE $PORT

# Instalar dependencias del sistema y limpiar después
RUN apt-get update && apt-get install --no-install-recommends -qy \
    git curl bash ca-certificates gnupg libxml2-dev libxslt-dev build-essential unzip \
    && curl -fsSL https://bun.sh/install | bash \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copiar binarios de UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copiar solo los archivos necesarios para la instalación de dependencias
COPY uv.lock pyproject.toml /app/

# Instalar dependencias sin caché ni paquetes de desarrollo
RUN uv sync --frozen --no-cache --no-dev

# Copiar el resto del código después para aprovechar la caché de dependencias
COPY . /app/

CMD ["uv", "run", "python", "-m", "pelican", "-lr", "/app/content", "-o", "/app/output", "-s", "/app/pelicanconf.py", "-p", "8000", "-b", "0.0.0.0"]
