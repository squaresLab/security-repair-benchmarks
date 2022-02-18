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

ARG SUT_REPO_URL=https://gitlab.gnome.org/GNOME/libxml2.git
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
RUN REPAIR_TOOL=none bear ./prebuild
RUN REPAIR_TOOL=none bear ./build

RUN if [ -e MYBUG.cfg ]; then cp MYBUG.cfg BUG.cfg; fi

WORKDIR /benchmarks/SanitizerResults
RUN python3 gen_llvm.py

WORKDIR /workspace
