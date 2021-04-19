FROM ubuntu:16.04

COPY --from=extractfix /opt/ /opt/

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      autoconf \
      automake \
      autopoint \
      bison \
      build-essential \
      clang \
      flex \
      gettext \
      git \
      gperf \
      ipython \
      libjpeg-dev \
      libtool \
      python-dev \
      python-pip \
      python3-dev \
      python3-pip \
      rsync \
      texinfo \
      unzip \
      vim \
      zip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

RUN pip install setuptools==42.0.2 \
 && pip install wllvm==1.2.8

# more run-time dependencies for extractfix
# TODO this should be included in the ExtractFix image in the /opt/extractfix/lib/python2.7/site-packages
# directory [and added to the PYTHONPATH by the extractfix wrapper]
RUN pip install \
      coloredlogs==15.0 \
      enum==0.4.7 \
 && pip3 install \
      pyparsing==2.4.7 \
      setuptools==56.0.0 \
      z3-solver==4.8.10.0

ENV EXTRACTFIX_BINARY /opt/extractfix/bin/extractfix

COPY --from=jasper-cve_2016_8691 /workspace /benchmarks/jasper/cve_2016_8691

COPY docker/repair /opt/secbugs/bin
ENV PATH "/opt/secbugs/bin:${PATH}"

#FROM ubuntu:xenial-20210114 AS xenial-builder
# FROM ubuntu:focal-20210217
# ENV DEBIAN_FRONTEND noninteractive
# ENV LANG C.UTF-8
# ENV LC_ALL C.UTF-8
# RUN apt-get update \
#  && apt-get install -y --no-install-recommends \
#         bear \
#         binutils-gold \
#         build-essential \
#         cmake \
#         curl \
#         file \
#         gcc \
#         git \
#         gpg-agent \
#         g++ \
#         musl-dev \
#         ninja-build \
#         shared-mime-info \
#         software-properties-common \
#         pkg-config \
#         python \
#         python3 \
#         python3-pip \
#         vim \
#         wget \
#         zlib1g-dev
# RUN pip3 install pip==20.3.4 \
#  && pip3 install setuptools==42.0.2 \
#  && pip3 install wllvm==1.2.8
# 
# # TODO we will need to install different version of llvm
# RUN curl -fsSL https://apt.llvm.org/llvm-snapshot.gpg.key | apt-key add - \
#  && echo "deb http://apt.llvm.org/focal/ llvm-toolchain-focal-12 main" >> /etc/apt/sources.list \
#  && echo "deb-src http://apt.llvm.org/focal/ llvm-toolchain-focal-12 main" >> /etc/apt/sources.list \
#  && apt-get update \
#  && apt-get install -y --no-install-recommends \
#         clang-12 \
#         libboost-all-dev \
#         libc++-12-dev \
#         libc++abi-12-dev \
#         libllvm-12-ocaml-dev \
#         lld-12 \
#         lldb-12 \
#         llvm-12-dev
# 
# ENV LLVM_COMPILER clang
# ENV LLVM_CC_NAME clang-12
# ENV LLVM_CXX_NAME clang++-12
# ENV CC wllvm
# ENV CXX wllvm++



