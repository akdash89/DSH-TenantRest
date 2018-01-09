FROM alpine:3.7

RUN apk add --no-cache git openssh-client curl unzip bash nano sudo ttf-dejavu coreutils

RUN apk add --no-cache python && \
    python -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip install --upgrade pip setuptools && \
    rm -r /root/.cache

RUN pip install virtualenv

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