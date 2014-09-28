#!/usr/bin/env python

import glob
import json
import argparse
import elasticsearch.helpers as esh
from elasticsearch import Elasticsearch

def list_json_directory(directory):
  return glob.glob(directory + '/*.json')

def read_json_from_file(json_file):
  return json.load(open(json_file))

def read_jsons_from_directory(directory):
  for json_file in list_json_directory(directory):
    yield read_json_from_file(json_file)

def new_es_client(hosts):
  es_hosts = [{'host':host,'port':ES_PORT} for host in args.hosts]
  return Elasticsearch(es_hosts)

def bulk_upload(es_client, json_documents, index, doc_id=None, bulk_size=1000):  
  if doc_id == None:
    actions = [{'_type':'doc','_source':document} for document in json_documents]
  else:
    actions = [{'_type':'doc','_id':document[doc_id],'_source':document} for document in json_documents]
  return esh.streaming_bulk(es, actions, index=index, chunk_size=bulk_size)


ES_PORT=9200

parser = argparse.ArgumentParser(prog='./es-upload.py', description='Upload a directory of JSON files to an elasticsearch cluster.')
parser.add_argument('--hosts', dest='hosts', nargs='+', type=str, help='A list of one or more host names or IPs, space-separated', required=True)
parser.add_argument('--jsondir', dest='directory', help='Directory of JSON files to be uploaded', required=True)
parser.add_argument('--index', dest='index', help='Index name')
parser.add_argument('--bulksize', dest='bulksize', type=int, default=1000, help='Number of documents in each bulk upload')
parser.add_argument('--deleteIndex', dest='deleteIndex', action='store_false', default=False, help='Delete index before uploading')
parser.add_argument('--id', dest='id', help='Field to use as document ID')
args = parser.parse_args()

json_documents = read_jsons_from_directory(args.directory)

es = new_es_client(args.hosts)

if args.deleteIndex:
  es.indices.delete(args.index)

for ok, result in bulk_upload(es, json_documents, args.index, args.id):
  print ok, result

