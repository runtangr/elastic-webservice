#encoding=utf-8
'''
@author: tangr
'''

from elasticsearch import Elasticsearch
import json
import datetime

date = datetime.datetime.now()
date_str = date.strftime("%Y.%m.%d")
index = "logstash-{0}".format()

def get_es_data(es,step):
	#index body后期优化
	resp = es.search(index=index,body={"query": {"match_all": {}},"size":10,
  "from": step,
  "sort": [
    {
      "@timestamp": {
        "order": "asc"
      }
    }
  ]})
	return resp

def init_es():

	es = Elasticsearch([{'host': 'localhost', 'port': 9204}])
 	return es

def analyze_es_data(es_data):
	for hit in es_data['hits']['hits']:
		# print(hit["_source"])

		if u'rsstatus' not in hit["_source"]:
			hit["_source"][u'rsstatus'] = 0
	return es_data

def update_es_data(data):
	es = init_es()
	updateBody = {}
	es.update_by_query(index=index, body=updateBody)


if __name__ == '__main__':
	pass