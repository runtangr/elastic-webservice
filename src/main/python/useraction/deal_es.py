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
					"gt": start_date,
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
		a = (start_time - datetime.datetime(year=1970, month=1, day=1)).total_seconds()
		start_date = int(a*1000)

	end_date = int(time.time()) * 1000
	return start_date, end_date

def get_es_data(es,body):

	resp = es.search(index=index,body=body)
	return resp

def init_es():

	es = Elasticsearch([{'host': 'elasticsearch', 'port': 9200}])
 	return es



if __name__ == '__main__':
	pass