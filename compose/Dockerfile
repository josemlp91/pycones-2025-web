FROM python:3.8-slim

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV PORT=8000
EXPOSE $PORT


# Install node via instructions at https://github.com/nodesource/distributions
RUN apt-get update \
    && apt-get install --no-install-recommends -qy git curl bash ca-certificates gnupg

    RUN apt update && apt install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt install -y nodejs \
    && apt clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /
RUN pip install -r /requirements.txt


WORKDIR /project-root

COPY compose/develop_server.sh /
RUN chmod +x /develop_server.sh

CMD /develop_server.sh start $PORT
