FROM base
RUN pip3 install meson==0.57.1
COPY src /experiment/src
COPY testcase /experiment/testcase
RUN pip3 install \
      jinja2==2.11.3 \
      markdown==3.3.4 \
      markupsafe==1.1.1 \
      toml==0.10.2 \
      typogrify==2.0.7
COPY testcase /experiment/testcase
COPY src /experiment/src

# for a given binary:
# extract-bc gdk-pixbuf-pixdata -l llvm-link-12

#      --default-library=static \
WORKDIR /experiment
RUN cd src \
 && meson build \
      --prefix=/experiment/prefix \
      --libdir=lib \
 && cd build \
 && ninja \
 && ninja install

COPY harness /experiment/harness
