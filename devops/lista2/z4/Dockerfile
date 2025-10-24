FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y curl
FROM alpine
ENV ADMIN_USER="mark"
RUN echo $ADMIN_USER > ./mark
RUN unset ADMIN_USER
