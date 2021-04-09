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
      rsync \
      texinfo \
      unzip \
      vim \
      zip \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN pip install setuptools==42.0.2 \
 && pip install wllvm==1.2.8

COPY --from=jasper-cve_2016_8691 /workspace /benchmarks/jasper/cve_2016_8691
