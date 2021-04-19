FROM ubuntu:16.04

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      bison \
      build-essential \
      clang \
      flex \
      git \
      ipython \
      libtool \
      python-dev \
      python-pip \
      texinfo \
      unzip \
      vim \
      zip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
COPY build build
COPY prebuild prebuild

ARG SUT_SOURCE_PATH=/workspace/source
RUN git clone git://sourceware.org/git/binutils-gdb.git "${SUT_SOURCE_PATH}"
ARG SUT_VERSION
RUN git -C "${SUT_SOURCE_PATH}" checkout "${SUT_VERSION}"

ARG BUG_DIR
COPY "${BUG_DIR}/exploit" exploit
COPY "${BUG_DIR}/test" test
COPY "${BUG_DIR}/bug.json" bug.json
