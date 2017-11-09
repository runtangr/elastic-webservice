#encoding=utf-8
'''
@author: tangr
'''

from elasticsearch import Elasticsearch
from useraction import deal_es
from useraction import deal_es_status
from useraction import deal_es2crm
import time

if __name__ == '__main__':
	
    es = deal_es.init_es()
    start_time = None

    while True:
        #获取es数据
        start_date, end_date = deal_es.get_date(start_time=start_time)
        body = deal_es.get_es_body(start_date, end_date)
        es_data = deal_es.get_es_data(es,body=body)

        if len(es_data["hits"]["hits"])==0:
            break

        print ("es_data = {0}".format(es_data))

        crm_datas = deal_es_status.deal_es_data(es_data)
        #存储数据到crm
        map(lambda crm_data:deal_es2crm.send_data(crm_data),crm_datas)

        start_time = deal_es_status.deal_es_timestamp(es_data)

