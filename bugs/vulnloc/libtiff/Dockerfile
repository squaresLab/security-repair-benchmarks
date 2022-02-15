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
      apt-transport-https \
      ca-certificates \
      wget \
      llvm \
      software-properties-common \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update \
 && add-apt-repository ppa:ubuntu-toolchain-r/test \
 && wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key| apt-key add -  \
 && apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-11 main" \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      clang-11

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
COPY getSanitizerInfo.sh getSanitizerInfo.sh

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

#RUN REPAIR_TOOL=none bear ./prebuild && REPAIR_TOOL=none bear ./build
RUN ln -sf /usr/bin/llvm-symbolizer-3.8 /usr/bin/llvm-symbolizer
RUN bash getSanitizerInfo.sh

COPY asan_symbolize.py /benchmarks/SanitizerResults/asan_symbolize.py
COPY sanitizer_parser.py /benchmarks/SanitizerResults/sanitizer_parser.py
WORKDIR /benchmarks/SanitizerResults

RUN chmod +x asan_symbolize.py
RUN chmod +x sanitizer_parser.py
#RUN ./asan_symbolize.py < / < addressSan.txt | c++filt > addressSan.output
RUN ./asan_symbolize.py < / < bothSan.txt | c++filt > bothSan.output
#RUN ./asan_symbolize.py < / < undefinedSan.txt | c++filt > undefinedSan.output
RUN ./sanitizer_parser.py

WORKDIR /workspace
RUN ./clean
RUN REPAIR_TOOL=none bear ./prebuild && REPAIR_TOOL=none bear ./build
RUN if [ -e MYBUG.cfg ]; then mv MYBUG.cfg BUG.cfg; fi
