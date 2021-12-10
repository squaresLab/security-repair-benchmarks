FROM ubuntu:16.04

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      autoconf \
      automake \
      autopoint \
      bear \
      bison \
      build-essential \
      clang \
      flex \
      gettext \
      git \
      gperf \
      jq \
      gcovr \
      ipython \
      jq \
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
COPY clean clean
COPY prebuild prebuild
COPY recompile recompile
COPY extractfix/project_specific_lib project_specific_lib

ARG BUG_DIR
COPY "${BUG_DIR}/" .

RUN [ "${SUT_GET_CODE_FROM_ARCHIVE}" = no ] \
 && git clone "${SUT_REPO_URL}" "${SUT_SOURCE_PATH}" \
 && git -C "${SUT_SOURCE_PATH}" checkout "${SUT_VERSION}" \
 || exit 0

RUN [ "${SUT_GET_CODE_FROM_ARCHIVE}" = yes ] \
 && cd /workspace \
 && unzip source.zip \
 && rm source.zip \
 || exit 0

RUN REPAIR_TOOL=none bear ./prebuild && REPAIR_TOOL=none bear ./build

RUN if [ -e MYBUG.cfg ]; then mv MYBUG.cfg BUG.cfg; fi
