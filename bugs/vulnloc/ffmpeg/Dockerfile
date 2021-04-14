FROM ubuntu:16.04

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      autoconf \
      automake \
      autopoint \
      bison \
      build-essential \
      clang \
      dh-autoreconf \
      flex \
      gettext \
      git \
      gperf \
      ipython \
      libass-dev \
      libmp3lame-dev \
      libtool \
      pkg-config \
      python-dev \
      python-pip \
      nasm \
      rsync \
      texinfo \
      unzip \
      valgrind \
      vim \
      wget \
      zip \
      zlib1g-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

ARG SUT_REPO_URL=https://github.com/gdraheim/zziplib.git
ARG SUT_SOURCE_PATH=/workspace/source
RUN git clone "${SUT_REPO_URL}" "${SUT_SOURCE_PATH}"

COPY build build
COPY prebuild prebuild

ARG SUT_VERSION
RUN git -C "${SUT_SOURCE_PATH}" checkout "${SUT_VERSION}"

ARG BUG_DIR
COPY "${BUG_DIR}/exploit" exploit
COPY "${BUG_DIR}/test" test
