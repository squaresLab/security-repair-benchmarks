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
      libtool \
      pkg-config \
      python-dev \
      python-pip \
      rsync \
      texinfo \
      unzip \
      vim \
      wget \
      zip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY build build
COPY prebuild prebuild

ARG SUT_DOWNLOAD_URL=https://libarchive.org/downloads/libarchive-3.2.0.zip
RUN wget -nv -O source.zip "${SUT_DOWNLOAD_URL}" \
 && unzip source.zip \
 && rm source.zip \
 && mv libarchive-* source

ARG BUG_DIR
COPY "${BUG_DIR}/exploit.zip" exploit.zip
COPY "${BUG_DIR}/test" test
RUN unzip exploit.zip -d exploit \
 && rm exploit.zip
