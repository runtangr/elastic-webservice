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
    #初始化步长

    # 获取步长
    es_step = deal_status.up_rsstatus()
    while True:
        #获取es数据
        es_data = deal_es.get_es_data(es,step=es_step)
        es_step += 10

        #过滤数据

        #存储数据到crm
        map(lambda crm_data:send_es2crm.send_data(crm_data),crm_datas)

        #设置步长
        es_data = deal_status.up_rsstatus(es_step)




    print(es_status_data)