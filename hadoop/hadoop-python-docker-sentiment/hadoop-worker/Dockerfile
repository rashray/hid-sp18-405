# Hadoop 2.9.0 cluster on Docker with Python Map-Reduce through Hadoop-streaming
#
# Application: sentiment analysis on movie review (Polarity 2.0 data)
#
# This Dockerfile creates image for worker node
# 
# docker build  -t minchen57/hadoop-python-docker-sentiment-master .
#
# Modified from sequenceiq/hadoop-docker <https://github.com/sequenceiq/hadoop-docker>
# Modified from Lewuathe/docker-hadoop-cluster <https://github.com/Lewuathe/docker-hadoop-cluster>

FROM minchen57/hadoop-docker-python-sentiment-compose-base:latest
MAINTAINER Min Chen

RUN service sshd start
ADD bootstrap.sh /etc/bootstrap.sh
RUN chown root:root /etc/bootstrap.sh
RUN chmod 700 /etc/bootstrap.sh

ENV BOOTSTRAP /etc/bootstrap.sh

CMD ["/etc/bootstrap.sh", "-d"]
