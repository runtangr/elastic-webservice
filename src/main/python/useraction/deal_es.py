#encoding=utf-8
'''
@author: tangr
'''

from elasticsearch import Elasticsearch
import json
import datetime
import time

date = datetime.datetime.now()
date_str = date.strftime("%Y.%m.%d")
index = "logstash-{0}".format(date_str)

def get_es_body(start_date, end_date):
	body = {
		"query": {
			"range": {
				"@timestamp": {
					"gte": start_date,
					"lt": end_date
				}
			}

		},
		"size": 5,
		"sort": [
			{
				"@timestamp": {
					"order": "asc"
				}
			}
		]
	}
	return body

def get_date(start_time=None):
	if start_time == None:
		start_time = datetime.datetime.now() + datetime.timedelta(hours=-12)
		a = start_time.timetuple()
		start_date = int(time.mktime(a)) * 1000
	else:
		a = start_time.timetuple()
		start_date = int(time.mktime(a)) * 1000

	end_date = int(time.time()) * 1000
	return start_date, end_date

def get_es_data(es,body):

	resp = es.search(index=index,body=body)
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