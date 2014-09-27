#!/bin/bash

ES_HOST="localhost:9200"

INDEX=movies
DOC_TYPE=doc
TIMESTAMP_FIELD=release_date
FORMAT="YYYY-MM-dd"

curl -XPUT "http://$ES_HOST/$INDEX/$DOC_TYPE/_mapping" -d "{'$DOC_TYPE':{'properties':{'$TIMESTAMP_FIELD':{'format':'$FORMAT','type':'date'}}}}"
