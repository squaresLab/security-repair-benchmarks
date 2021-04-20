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

ARG SUT_GET_CODE_FROM_ARCHIVE=no
ARG SUT_REPO_URL=https://github.com/vadz/libtiff.git
ARG SUT_SOURCE_PATH=/workspace/source
ARG SUT_VERSION

COPY build build
COPY prebuild prebuild

ARG BUG_DIR
COPY "${BUG_DIR}/" .

RUN [ "${SUT_GET_CODE_FROM_ARCHIVE}" = no ] \
 && git clone "${SUT_REPO_URL}" "${SUT_SOURCE_PATH}" \
 && git -C "${SUT_SOURCE_PATH}" checkout "${SUT_VERSION}" \
 || exit 0

RUN [ "${SUT_GET_CODE_FROM_ARCHIVE}" = yes ] \
 && cd /workspace \
 && unzip source.zip \
 || exit 0
