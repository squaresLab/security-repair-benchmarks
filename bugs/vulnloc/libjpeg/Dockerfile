FROM ubuntu:16.04

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      autoconf \
      automake \
      autopoint \
      bison \
      build-essential \
      clang \
      cmake \
      flex \
      gettext \
      git \
      gperf \
      ipython \
      libtool \
      nasm \
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

ARG SUT_REPO_URL=https://github.com/libjpeg-turbo/libjpeg-turbo.git
ARG SUT_SOURCE_PATH=/workspace/source
RUN git clone "${SUT_REPO_URL}" "${SUT_SOURCE_PATH}"

COPY build build
COPY prebuild prebuild

# build the project-specific lib
COPY extractfix/project_specific_lib project_specific_lib
RUN cd project_specific_lib \
 && gcc -c -o hook.o hook.c \
 && ar rcs libhook.a hook.o \
 && rm hook.o

ARG SUT_VERSION
ARG SUT_USES_CMAKE=yes
RUN git -C "${SUT_SOURCE_PATH}" checkout "${SUT_VERSION}" \
 && cd "${SUT_SOURCE_PATH}" \
 && [ "${SUT_USES_CMAKE}" = no ] && autoreconf -fiv || exit 0

ARG BUG_DIR
COPY "${BUG_DIR}/" .

RUN wget -nv https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 \
     && chmod u+x jq-linux64 \
     && mv jq-linux64 /bin/jq

RUN REPAIR_TOOL=none bear ./prebuild \
 && REPAIR_TOOL=none bear ./build