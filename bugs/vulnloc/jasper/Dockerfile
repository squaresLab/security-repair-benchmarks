FROM ubuntu:16.04

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      autoconf \
      automake \
      autopoint \
      bison \
      build-essential \
      clang \
      flex \
      gettext \
      git \
      gperf \
      ipython \
      libjpeg-dev \
      libtool \
      python-dev \
      python-pip \
      rsync \
      texinfo \
      unzip \
      vim \
      zip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

ARG SUT_SOURCE_PATH=/workspace/source

COPY build build
COPY prebuild prebuild
COPY project_compile.sh project_compile.sh

ARG BUG_DIR
COPY "${BUG_DIR}/" .

RUN unzip source.zip \
 && rm source.zip \
 && cd "${SUT_SOURCE_PATH}" \
 && autoreconf -i
