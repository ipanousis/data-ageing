#!/bin/bash

ES_PY=es-upload.py
HOSTS=`es-cluster-ips 2`
INDEX=movies

$ES_PY --hosts `es-cluster-ips 2` --jsondir downloads/1900 --index movies --deleteIndex

for YEAR in `seq 1901 2020`; do
  $ES_PY --hosts $HOSTS --jsondir downloads/$YEAR --index movies
done
