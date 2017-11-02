#encoding=utf-8

from elasticsearch import Elasticsearch
import json

def get_es_data(es):

	resp = es.search(index='logstash-2017.10.31',body={"query": {"match_all": {}}})
	return resp

def init_es():

	es = Elasticsearch([{'host': '10.10.1.102', 'port': 9204}])
 	return es

def analyze_es_data(es_data):
	for hit in es_data['hits']['hits']:
		# print(hit["_source"])

		if u'rsstaus' not in hit["_source"]:
			hit["_source"][u'rsstaus'] = 0
	return es_data

# judge_status():


if __name__ == '__main__':
	pass