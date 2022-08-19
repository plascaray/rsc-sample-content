# Dockerfile ref: https://github.com/rstudio/rstudio-docker-products/blob/main/content/base/bionic/Dockerfile 

# Using dated tags from https://hub.docker.com/_/ubuntu/
FROM ubuntu:bionic
## todo: should I build from dev-connect so that I can make easy changes to the runtime dependencies?

LABEL Author="David Kegley <david.kegley@rstudio.com>"

# Installation prerequisites --------------------------------------------------#
# curl is used to download things.
# libev-dev is required for most interactive Python applications.
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y \
    curl \
    libev-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python --------------------------------------------------------------#
ARG MINICONDA_VERSION=4.7.12.1
ARG PYTHON_VERSION=3.8.2

# The documented approach uses a particular miniconda install script version
# to obtain the desired Python version. We are first installing miniconda and
# then asking it to install different Python versions.

RUN curl -fsSL -o miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-${MINICONDA_VERSION}-Linux-x86_64.sh \
    && chmod 755 miniconda.sh \
    && ./miniconda.sh -b -p /opt/miniconda \
    && /opt/miniconda/bin/conda create --quiet --yes --prefix /opt/python/${PYTHON_VERSION} python=${PYTHON_VERSION} virtualenv \
    && rm -f miniconda.sh \
    # remove miniconda too, for size
    && rm -rf /opt/miniconda

# TODO: These libraries are required by Connect but when should they be installed and who
# should be responsible for installing them? Should our runtime dependencies come with
# and requirements.txt file?
RUN /opt/python/${PYTHON_VERSION}/bin/pip install setuptools bjoern==3.1.0

# Install Connect Runtime Dependencies ----------------------------------------#
ARG RSC_VERSION=2022.07.0

RUN mkdir -p /opt/rstudio-connect \
    && RSC_VERSION_URL=`echo -n "${RSC_VERSION}" | sed 's/+/%2B/g'` \
    && curl -fsSL -o /tmp/rstudio-connect-runtime.tar.gz https://cdn.rstudio.com/connect/$(echo $RSC_VERSION | sed -r 's/([0-9]+\.[0-9]+).*/\1/')/rstudio-connect-runtime-${RSC_VERSION_URL}.tar.gz \
    && tar -C /opt/rstudio-connect -xf /tmp/rstudio-connect-runtime.tar.gz \
    && chmod 755 /opt/rstudio-connect \
    && rm /tmp/rstudio-connect-runtime.tar.gz

# Install App Content ---------------------------------------------------------#

# TODO: What should we do about the job directory? The output-timestamper requires that it exists and is writable
#   by the container user which we don't know a UID/GID for at build time.
RUN mkdir -p /opt/rstudio-connect/mnt/app \
    && mkdir -p /opt/rstudio-connect/mnt/job \
    && chmod 777 /opt/rstudio-connect/mnt/job

COPY app.py \
     manifest.json \
     requirements.txt \
     /opt/rstudio-connect/mnt/app/

RUN /opt/python/${PYTHON_VERSION}/bin/pip install -r /opt/rstudio-connect/mnt/app/requirements.txt
