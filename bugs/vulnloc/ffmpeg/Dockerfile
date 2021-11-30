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
      jq \
      gcovr \
      gperf \
      ipython \
      libass-dev \
      libfdk-aac-dev \
      libmp3lame-dev \
      libopus-dev \
      libtheora-dev \
      libvorbis-dev \
      libvpx-dev \
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

# build the project-specific lib
COPY extractfix/project_specific_lib project_specific_lib
RUN cd project_specific_lib \
 && gcc -c -o hook.o hook.c \
 && ar rcs libhook.a hook.o \
 && rm hook.o

WORKDIR /workspace
COPY build build
COPY prebuild prebuild

ARG SUT_REPO_URL=https://github.com/FFmpeg/FFmpeg.git
ARG SUT_SOURCE_PATH=/workspace/source
RUN git clone "${SUT_REPO_URL}" "${SUT_SOURCE_PATH}"
ARG SUT_VERSION
RUN git -C "${SUT_SOURCE_PATH}" checkout "${SUT_VERSION}"

COPY common/* "${SUT_SOURCE_PATH}/"

ARG BUG_DIR
COPY "${BUG_DIR}/" ./
