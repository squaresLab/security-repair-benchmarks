FROM ubuntu:16.04

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      bear \
      bison \
      build-essential \
      clang \
      flex \
      jq \
      gcovr \
      git \
      ipython \
      libtool \
      python-dev \
      python-pip \
      texinfo \
      unzip \
      vim \
      wget \
      zip \
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

COPY build build
COPY clean clean
COPY prebuild prebuild
COPY getSanitizerInfo.sh getSanitizerInfo.sh


ARG SUT_SOURCE_PATH=/workspace/source
RUN git clone git://sourceware.org/git/binutils-gdb.git "${SUT_SOURCE_PATH}"
ARG SUT_VERSION
RUN git -C "${SUT_SOURCE_PATH}" checkout "${SUT_VERSION}"

ARG BUG_DIR
COPY "${BUG_DIR}/" ./

RUN wget -nv https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 \
 && chmod u+x jq-linux64 \
 && mv jq-linux64 /bin/jq

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
RUN REPAIR_TOOL=none bear ./prebuild \
 && REPAIR_TOOL=none bear ./build

WORKDIR /benchmarks/SanitizerResults
RUN python3 gen_llvm.py

WORKDIR /workspace
