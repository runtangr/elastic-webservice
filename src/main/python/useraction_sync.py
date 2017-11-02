#encoding=utf-8

from elasticsearch import Elasticsearch
from useraction import get_es
from useraction import deal_status

'''
@author: tangr
'''

if __name__ == '__main__':
	
	es = get_es.init_es()
	#获取es数据
	es_data = get_es.get_es_data(es)
	#设置标志位，有就不设置，没有就设置为0
	es_status_data = get_es.analyze_es_data(es_data=es_data)
	#取出标志位为0的数据
	crm_data = deal_status.deal_status(es_status_data)
	#存储数据到crm

	print(es_status_data)