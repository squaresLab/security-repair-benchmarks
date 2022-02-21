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
      jq \
      gcovr \
      gettext \
      git \
      gperf \
      ipython \
      libtool \
      python-dev \
      python-pip \
      rsync \
      texinfo \
      unzip \
      vim \
      zip \
      wget \
      apt-transport-https \
      ca-certificates \
      llvm \
      software-properties-common \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

RUN apt-get update \
 && add-apt-repository ppa:ubuntu-toolchain-r/test \
 && wget -O - https://apt.llvm.org/llvm-snapshot.gpg.key| apt-key add -  \
 && apt-add-repository "deb http://apt.llvm.org/xenial/ llvm-toolchain-xenial-11 main" \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential \
      clang-11

ARG SUT_REPO_URL=https://github.com/coreutils/coreutils.git
ARG SUT_SOURCE_PATH=/workspace/source
RUN git clone "${SUT_REPO_URL}" "${SUT_SOURCE_PATH}"

COPY build build
COPY clean clean
COPY prebuild prebuild
COPY recompile recompile
COPY getSanitizerInfo.sh getSanitizerInfo.sh


# build the project-specific lib
COPY extractfix/project_specific_lib project_specific_lib
RUN cd project_specific_lib \
 && gcc -c -o hook.o hook.c \
 && ar rcs libhook.a hook.o \
 && rm hook.o

ARG SUT_VERSION
RUN cd "${SUT_SOURCE_PATH}" \
 && git checkout "${SUT_VERSION}"

ARG BUG_DIR
COPY "${BUG_DIR}/" ./
RUN ln -sf /usr/bin/llvm-symbolizer-3.8 /usr/bin/llvm-symbolizer
RUN bash getSanitizerInfo.sh

COPY asan_symbolize.py /benchmarks/SanitizerResults/asan_symbolize.py
COPY sanitizer_parser.py /benchmarks/SanitizerResults/sanitizer_parser.py
COPY gen_llvm.py /benchmarks/SanitizerResults/gen_llvm.py

WORKDIR /benchmarks/SanitizerResults

RUN chmod +x asan_symbolize.py
RUN chmod +x sanitizer_parser.py
RUN ./asan_symbolize.py < / < bothSan.txt | c++filt > bothSan.output
RUN ./sanitizer_parser.py


WORKDIR /workspace
RUN ./clean
RUN REPAIR_TOOL=none bear ./prebuild 
RUN REPAIR_TOOL=none bear ./build

RUN if [ -e MYBUG.cfg ]; then cp MYBUG.cfg BUG.cfg; fi

WORKDIR /benchmarks/SanitizerResults
RUN python3 gen_llvm.py

WORKDIR /workspace
RUN ./clean &&  REPAIR_TOOL=none ./prebuild && REPAIR_TOOL=none ./build
