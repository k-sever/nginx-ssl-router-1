#FROM ubuntu:trusty
FROM geerlingguy/docker-ubuntu1404-ansible:latest

RUN sudo apt-get update
RUN sudo apt-get -y install python-pip
RUN sudo pip install 'boto==2.38.0'
RUN pip install setuptools --upgrade

ADD . /nginx-ssl-router
WORKDIR /nginx-ssl-router


