#coding=utf-8
'''
Crate on 1 Nov 2017
@author:hcy7
'''

from elasticsearch import Elasticsearch
import json
from datetime import datetime

def deal_es_timestamp(es_data):
    #es_data = ds.get_es_data()
    datalen = len(es_data['hits']['hits'])
    data = es_data['hits']['hits'][datalen -1]
    datedata = data["_source"]['@timestamp']
    dt = datetime.strptime(datedata, "%Y-%m-%dT%H:%M:%S.%fZ")
    return dt

if __name__ == '__main__':
	pass
