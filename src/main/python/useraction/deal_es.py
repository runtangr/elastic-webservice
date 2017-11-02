#encoding=utf-8
'''
@author: tangr
'''

from elasticsearch import Elasticsearch
import json

def get_es_data(es):
	#index body后期优化
	resp = es.search(index='logstash-2017.10.31',body={"query": {"match_all": {}}})
	return resp

def init_es():

	es = Elasticsearch([{'host': '10.10.1.102', 'port': 9204}])
 	return es

def analyze_es_data(es_data):
	for hit in es_data['hits']['hits']:
		# print(hit["_source"])

		if u'rsstatus' not in hit["_source"]:
			hit["_source"][u'rsstatus'] = 0
	return es_data

def update_es_data(data):
	es = init_es()
	es.update(index='logstash-2017.10.31', doc_type='news', id=hit.meta.id,
				body={"doc": {"stanford": 1, "parsed_sents": parsed}})


if __name__ == '__main__':
	pass