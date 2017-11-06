#coding=utf-8
'''
Crate on 2 Nov 2017
@author:hcy7
'''

import unittest
from useraction import deal_es_status as ds
import data_of_test as td

class MyTestCase(unittest.TestCase):

    def set_data(self):
        self.deal_status_data = td.deal_es_data()
        self.up_status_data = td.up_es_data()

    def test_deal_es_status(self):
        self.set_data()
        print (ds.deal_es_timestamp(self.deal_status_data))

if __name__ == '__main__':
    unittest.main()