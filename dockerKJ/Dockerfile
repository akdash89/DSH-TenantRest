FROM openjdk:8u121-jdk-alpine
MAINTAINER "rpartapsing" <r.partapsing@gmail.com>
LABEL name="Docker image for Tenant with Jenkins"

ARG ssh_port=22

RUN apk add --no-cache git openssh-client curl gcc unzip bash nano ttf-dejavu coreutils libpcap-dev python3-tkinter docker

RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
  && apk add --update \
              musl \
              build-base \
              linux-headers \
              ca-certificates \
              python3 \
              python3-dev \
  && pip3 install --no-cache-dir --upgrade --force-reinstall pip \
  && rm /var/cache/apk/*

RUN cd /usr/bin \
  && ln -sf easy_install-3.5 easy_install \
  && ln -sf idle3.5 idle \
  && ln -sf pydoc3.5 pydoc \
  && ln -sf python3.5 python \
  && ln -sf python3.5-config python-config \
  && ln -sf pip3.5 pip

ADD requirements /py/requirements
ADD py /py
ADD templates /py/templates

WORKDIR /py

EXPOSE ${ssh_port}

RUN pip3 install -r /py/requirements/requirements.txt

RUN echo "done"