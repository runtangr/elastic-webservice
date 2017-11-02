#coding=utf-8
#test data

import json

def es_data():
    testdata = {u'hits':
    {u'hits':
    [
    {u'_score': 1.0, u'_type': u'technical', u'_id': u'AV9wC_MRAKfszuCEfWJg',
	u'_source':
	{u'ident': u'10272017948', u'@version': u'1', u'referrer': u'"PC"',u'@timestamp': u'2017-10-31T01:29:12.197Z',u'request': u'/zhibodt/213831280/zhibo/kp10270956/tearcher/cf102709271',u'auth': u'-', u'response': u'200', u'bytes': 58, u'host': u'172.23.0.1 ', u'verb': u'GET',u'agent': u'"python-requests/2.18.1"', u'rsstatus': 0, u'timestamp': u'27/Oct/2017:08:50:00 +0800',u'message': u'113.201.30.129 10272017948 - [27/Oct/2017:08:50:00 +0800] "GET /zhibodt/213831280/zhibo/kp10270956/tearcher/cf102709271 HTTP/1.1" 200 58 "PC" "python-requests/2.18.1" "-" "cdhq.zqf.com.cn "',u'type': u'technical', u'port': 34694, u'clientip': u'113.201.30.129 ', u'httpversion': u'1.1'},
    u'_index': u'logstash-2017.10.31'},
    {
    u'_score': 1.0, u'_type': u'technical', u'_id': u'AV9wC8JYAKfszuCEfWJc',
    u'_source':
    {u'ident': u'102117302017', u'@version': u'1', u'referrer': u'"web"', u'@timestamp': u'2017-10-31T01:28:59.611Z', u'request': u'/article/102117308', u'auth': u'-', u'response': u'200', u'bytes': 58, u'host': u'172.23.0.1 ', u'verb': u'GET', u'agent': u'"python-requests/2.18.1"', u'rsstatus': 0, u'timestamp': u'21/Oct/2017:17:30:00 +0800', u'message': u'223.81.195.163 102117302017 - [21/Oct/2017:17:30:00 +0800] "GET /article/102117308 HTTP/1.1" 200 58 "web" "python-requests/2.18.1" "-" "cdhq.zqf.com.cn"', u'type': u'technical', u'port': 34682, u'clientip': u'223.81.195.163', u'httpversion': u'1.1'},
     u'_index': u'logstash-2017.10.31'}
    ]
    }
    }
    return testdata

if __name__ == '__main__':
	pass