FROM ubuntu:16.04

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
COPY build build
COPY prebuild prebuild

# build the project-specific lib
COPY extractfix/project_specific_lib project_specific_lib
RUN cd project_specific_lib \
 && gcc -c -o hook.o hook.c \
 && ar rcs libhook.a hook.o \
 && rm hook.o

ARG SUT_DOWNLOAD_URL=https://libarchive.org/downloads/libarchive-3.2.0.zip
RUN wget -nv -O source.zip "${SUT_DOWNLOAD_URL}" \
 && unzip source.zip \
 && rm source.zip \
 && mv libarchive-* source

# fixes libtool compatibility issue
#
# > make[1]: Entering directory '/tmp/proj_work_dir_._1619722450/source/klee'
# >   CC       libarchive/archive_acl.lo
# > libtool: Version mismatch error.  This is libtool 2.4.2 Debian-2.4.2-1.11, but the
# > libtool: definition of this LT_INIT comes from libtool 2.4.6.
# > libtool: You should recreate aclocal.m4 with macros from libtool 2.4.2 Debian-2.4.2-1.11
# > libtool: and run autoconf again.
# > Makefile:5460: recipe for target 'libarchive/archive_acl.lo' failed
RUN cd source \
 && autoreconf -fi

ARG BUG_DIR
COPY "${BUG_DIR}/" ./
RUN unzip exploit.zip -d exploit \
 && rm exploit.zip
