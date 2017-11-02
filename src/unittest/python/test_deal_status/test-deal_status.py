#coding=utf-8
'''
Crate on 2 Nov 2017
@author:hcy7
'''

import unittest
from useraction import deal_status as ds
import test_data as td

class MyTestCase(unittest.TestCase):

    def set_data(self):
        self.data = td.es_data()
        print (self.data)
    def test_deal_status(self):
        self.set_data()
        print (ds.deal_status(self.data))


if __name__ == '__main__':
    unittest.main()