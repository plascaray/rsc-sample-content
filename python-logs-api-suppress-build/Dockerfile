FROM python:3.10.6-slim-bullseye
LABEL Author="David Kegley <david.kegley@rstudio.com>"

# TODO: How should we document these required dependencies that are normally installed by connect?
# https://github.com/rstudio/connect/blob/c560fea45e47bd6ca6cc4c23efdb5d4b3a796f9c/python/build_environment.py#L280-L288

RUN set -eux; \
    savedAptMark="$(apt-mark showmanual)"; \
    apt-get update; \
    apt-get install -y --no-install-recommends libc6-dev libev-dev gcc; \
    pip install --no-cache-dir waitress==1.4.3 bjoern==3.1.0; \
    apt-mark auto '.*' > /dev/null; \
    [ -z "$savedAptMark" ] || apt-mark manual $savedAptMark > /dev/null; \
    apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
    rm -rf /var/lib/apt/lists/*;

# Install the content dependencies to the local python environment
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt; \
    rm /tmp/requirements.txt
