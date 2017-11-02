#encoding=utf-8

from elasticsearch import Elasticsearch
from useraction import get_es

'''
@author: tangr
'''

if __name__ == '__main__':
	
	es = get_es.init_es()
	es_data = get_es.get_es_data(es)
	es_status_data = get_es.analyze_es_data(es_data=es_data)


	print(es_status_data)