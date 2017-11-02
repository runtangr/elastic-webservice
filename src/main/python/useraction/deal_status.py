#coding=utf-8
'''
Crate on 1 Nov 2017
@author:hcy7
'''

from elasticsearch import Elasticsearch
import json

def deal_status(es_data):
    source_data = []
    for hit in es_data['hits']['hits']:
        datalen = len(es_data['hits']['hits'])
        for i in range(datalen):
            if es_data['hits']['hits'][i]['_source']['rsstatus'] == 0:
                sourcedt = es_data['hits']['hits'][i]['_source']
            source_data.append(sourcedt)
    return source_data

if __name__ == '__main__':
	pass
