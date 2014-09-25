FROM ubuntu:14.04

RUN apt-get update

# Install java
RUN apt-get -y install software-properties-common
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections
RUN apt-get -y install oracle-java8-installer
RUN rm -rf /var/lib/apt/lists/*
 
# Install Runit
RUN apt-get update
RUN apt-get install -y runit

# Install sshd
RUN apt-get -y install openssh-server
RUN mkdir -p /var/run/sshd && echo 'root:root' | chpasswd
RUN sed -i "s/session.*required.*pam_loginuid.so/#session    required     pam_loginuid.so/" /etc/pam.d/sshd
RUN sed -i "s/PermitRootLogin without-password/#PermitRootLogin without-password/" /etc/ssh/sshd_config

ADD sv /etc/service

CMD /usr/sbin/runsvdir-start
