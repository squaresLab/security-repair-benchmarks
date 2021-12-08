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

ARG SUT_REPO_URL=https://gitlab.gnome.org/GNOME/libxml2.git
ARG SUT_SOURCE_PATH=/workspace/source
RUN git clone "${SUT_REPO_URL}" "${SUT_SOURCE_PATH}"

COPY build build
COPY clean clean
COPY prebuild prebuild
COPY recompile recompile

# build the project-specific lib
COPY extractfix/project_specific_lib project_specific_lib
RUN cd project_specific_lib \
 && gcc -c -o hook.o hook.c \
 && ar rcs libhook.a hook.o \
 && rm hook.o

ARG SUT_VERSION
RUN git -C "${SUT_SOURCE_PATH}" checkout "${SUT_VERSION}"

ARG BUG_DIR
COPY "${BUG_DIR}/" ./

RUN wget -nv https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 \
 && chmod u+x jq-linux64 \
 && mv jq-linux64 /bin/jq

RUN REPAIR_TOOL=none bear ./prebuild
RUN REPAIR_TOOL=none bear ./build

RUN if [ -e MYBUG.cfg ]; then cp MYBUG.cfg BUG.cfg; fi
