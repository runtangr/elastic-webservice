#coding=utf-8
'''
Crate on 1 Nov 2017
@author:hcy7
'''

from elasticsearch import Elasticsearch
import json
from datetime import datetime
from deal_es import init_es

def deal_status_rsstatus(es_data):
    source_data = []
    for hit in es_data['hits']['hits']:
        datalen = len(es_data['hits']['hits'])
        for i in range(datalen):
            if es_data['hits']['hits'][i]['_source']['rsstatus'] == 0:
                sourcedt = es_data['hits']['hits'][i]['_source']
            source_data.append(sourcedt)
    return source_data

def up_rsstatus(es_data):
    dtlen = len(es_data)
    for i in range(dtlen):
        if es_data[i]['rsstatus'] == 0:
            es_data[i]['rsstatus'] = 1
    return es_data

def init_step():
    es = init_es()
    doc = {
        "step":0,
        "timestamp":datetime.now()
    }
    es_res = es.indices.create(index = "step", body = doc)
    return es_res

def get_step():
    es = init_es()
    res = es.search(index = 'step', body={"query": {"match_all": {}}})
    return res


if __name__ == '__main__':
	pass
