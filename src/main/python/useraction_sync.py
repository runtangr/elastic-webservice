#encoding=utf-8
'''
@author: tangr
'''

from elasticsearch import Elasticsearch
from useraction import deal_es
from useraction import deal_status
from useraction import send_es2crm

if __name__ == '__main__':
	
    es = deal_es.init_es()
    #获取es数据
    es_data = deal_es.get_es_data(es)
    #设置标志位，有就不设置，没有就设置为0
    es_status_data = deal_es.analyze_es_data(es_data=es_data)
    #取出标志位为0的数据
    crm_datas = deal_status.deal_status(es_status_data)
    #存储数据到crm
    map(lambda crm_data:send_es2crm.send_data(crm_data),crm_datas)

    #设置标志位为1

    #更新es数据
    deal_es.update_es_data(data=crm_datas)

    print(es_status_data)