FROM ubuntu:16.04
MAINTAINER "rpartapsing" <r.partapsing@gmail.com>
LABEL name="Docker image for Tenant with Jenkins"

ARG ssh_port=22

RUN apt-get update && apt-get install -y \
    libssl-dev \
    libffi-dev \
    python3 \
    python3-dev \
    python3-pip \
    python3-tk \
    libltdl7 \
    libxslt1-dev \
    git \
&& apt-get clean

ADD requirements /py/requirements
ADD py /py
ADD templates /py/templates

WORKDIR /py

EXPOSE ${ssh_port}

RUN pip3 install -r /py/requirements/requirements.txt

RUN echo "done"
