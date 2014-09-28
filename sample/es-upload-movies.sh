#!/bin/bash

ES_PY=es-upload.py
HOSTS=`es-cluster-ips 2`
INDEX=movies
ID=id

$ES_PY --hosts $HOSTS --jsondir downloads/1900 --index $INDEX --id $ID --deleteIndex

for YEAR in `seq 1901 2020`; do
  $ES_PY --hosts $HOSTS --jsondir downloads/$YEAR --index $INDEX --id $ID
done

