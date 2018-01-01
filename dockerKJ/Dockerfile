FROM openjdk:8u121-jdk-alpine
MAINTAINER "rpartapsing" <r.partapsing@gmail.com>
LABEL name="Docker image for Tenant with Jenkins"

ARG ssh_port=22

RUN apk add --no-cache git openssh-client curl unzip bash nano ttf-dejavu coreutils
RUN apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

ADD requirements /py/requirements
ADD py /py

WORKDIR /py

EXPOSE ${ssh_port}

RUN pip install -r /robot/requirements/requirements.txt
RUN echo "done"