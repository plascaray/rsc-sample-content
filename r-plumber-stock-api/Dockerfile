# Used for hack-week Aug 2021

# This is a stripped-down version of the official RStudio content-base image (no python, no extra libs)
#  https://github.com/rstudio/rstudio-docker-products/blob/main/content/base/bionic/Dockerfile
FROM ubuntu:bionic

RUN export DEBIAN_FRONTEND=noninteractive && \
  apt-get update \
  && apt-get install -y \
  git \
  curl \
  libcurl4-openssl-dev \
  libev-dev \
  libsodium-dev \
  && rm -rf /var/lib/apt/lists/*

# Install R ------------------------------------------------------------------ #
# Reference: https://docs.rstudio.com/resources/install-r/
ARG R_DISTRIBUTION=ubuntu-1804

ARG R_VERSION=3.6.3
ARG R_INSTALLER=r-${R_VERSION}_1_amd64.deb
RUN curl -fsSL -O https://cdn.rstudio.com/r/${R_DISTRIBUTION}/pkgs/${R_INSTALLER} && \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -f -y ./${R_INSTALLER} && \
    rm ${R_INSTALLER} && \
    rm -rf /var/lib/apt/lists/*
    
#RUN export DEBIAN_FRONTEND=noninteractive && \
#  apt-get update \
#  && \
#  apt-get install -y \
#  gdal-bin \
#  libgdal-dev \
#  && \
#  rm -rf /var/lib/apt/lists/*
