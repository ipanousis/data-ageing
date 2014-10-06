FROM ypanousi/elasticsearch
 
# Kibana
RUN curl https://download.elasticsearch.org/kibana/kibana/kibana-4.0.0-BETA1.tar.gz | tar xz
RUN mv kibana-4.0.0-BETA1 /kibana

# Elasticsearch Plugins
RUN /elasticsearch/bin/plugin -install mobz/elasticsearch-head 
RUN /elasticsearch/bin/plugin -install elasticsearch/marvel/latest
RUN /elasticsearch/bin/plugin -install karmi/elasticsearch-paramedic

# Logstash
#RUN curl https://download.elasticsearch.org/logstash/logstash/logstash-1.4.1.tar.gz | tar xz 
#java -jar logstash-1.2.2-flatjar.jar agent -f docker-kibana/logstash.conf

ADD sv /etc/service

EXPOSE 5601 9200

CMD /usr/sbin/runsvdir-start
