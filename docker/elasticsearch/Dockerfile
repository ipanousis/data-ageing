FROM ypanousi/runit-ssh-java 

RUN apt-get -y install curl

# ElasticSearch
RUN curl https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.3.2.tar.gz | tar xz && \
    mv elasticsearch-* /elasticsearch

ADD sv /etc/service

EXPOSE 9200

CMD /usr/sbin/runsvdir-start
