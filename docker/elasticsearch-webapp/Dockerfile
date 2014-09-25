FROM ypanousi/elasticsearch
 
# Install apache
RUN apt-get install -y apache2

# Kibana
RUN curl https://download.elasticsearch.org/kibana/kibana/kibana-3.1.0.tar.gz | tar xz && \
    mv kibana-* /kibana
RUN sed -i -e 's|elasticsearch:.*|elasticsearch: "http://" + window.location.hostname + ":" + 9200,|' /kibana/config.js
RUN rm -rf /var/www/html/*
RUN cp -rf /kibana/* /var/www/html/

# Elasticsearch Plugins
RUN /elasticsearch/bin/plugin -install mobz/elasticsearch-head 
RUN /elasticsearch/bin/plugin -install elasticsearch/marvel/latest
RUN /elasticsearch/bin/plugin -install karmi/elasticsearch-paramedic

# Logstash
#RUN curl https://download.elasticsearch.org/logstash/logstash/logstash-1.4.1.tar.gz | tar xz 
#java -jar logstash-1.2.2-flatjar.jar agent -f docker-kibana/logstash.conf

ADD sv /etc/service

EXPOSE 80 9200

CMD /usr/sbin/runsvdir-start
