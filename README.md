data-ageing
===========

Aggregation of events over time

The initial intention of this project was to perform a form of data retention by doing an automated aggregation 
over time in ElasticSearch, based on some straightforward ElasticSearch index configuration files.

At the moment however this work is distracted by an exciting turn towards flexible building of multi-host docker clusters.
A new tool called Flocker (https://github.com/clusterhq/flocker) is still young but a very easy to use way of managing the
much-assorted concept of a multi-host docker cluster. It is one alternative to what is offered by CoreOS, except un-restricted
to a specific Linux distribution, while also making it simpler to utilise services running on the cluster from the outside.

So, using Vagrant, Google Cloud, Flocker and NodeJS some first steps are being made to write a simple UI to leverage what is
offered by Flocker through the CLI.
