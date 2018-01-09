FROM ubuntu:16.04
MAINTAINER "rpartapsing" <r.partapsing@gmail.com>
LABEL name="Docker image for Robot Framework inside venv"

RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get -y update && apt-get upgrade -y
RUN apt-get install python build-essential python-dev python-pip python-setuptools -y
RUN apt-get install libxml2-dev libxslt1-dev python-dev -y
RUN apt-get install iputils-ping ssh curl net-tools netcat -y
RUN apt-get install vim -y
RUN pip install virtualenv uwsgi
RUN apt-get install sudo -y

USER root
ADD sudoers.txt /etc/sudoers
RUN chmod 440 /etc/sudoers

#ADD Testcases /robot/Testcases
ADD requirements /robot/requirements
ADD runscript.sh /robot
RUN chmod 777 /robot/runscript.sh
#ADD Testresults /robot/Testresults

VOLUME Testcases
VOLUME Testresults

RUN virtualenv /robot/venv
RUN source /robot/venv/bin/activate && pip install -r /robot/requirements/requirements.txt
RUN echo "done"