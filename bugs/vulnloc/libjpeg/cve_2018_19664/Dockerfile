FROM ubuntu:16.04

RUN git clone https://github.com/libjpeg-turbo/libjpeg-turbo.git
RUN mv libjpeg-turbo source
WORKDIR /root/source
RUN git checkout beefb62
RUN export CXXFLAGS="-ggdb"
RUN export CFLAGS="-ggdb"
RUN cmake CMakeLists.txt
RUN make

COPY ./exploit /root/exploit

