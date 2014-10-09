FROM ipanousis/runit-ssh-java 

RUN apt-get -y install curl

RUN curl https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.0.Beta1.tar.gz | tar xz && \
    mv elasticsearch-* /elasticsearch

ADD sv /etc/service

EXPOSE 9200

CMD /usr/sbin/runsvdir-start
