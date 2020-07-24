import unittest
import requests
import os, sys

class GetEventListTest(unittest.TestCase):

    def setUp(self):
        self.baseurl = 'http://127.0.0.1:8000/api/get_event_list/'

    def tearDown(self) -> None:
        print(self.result)
    def test_get_event_list_eid_error(self):
        '''eid not exist'''
        r = requests.get(self.baseurl, params={'eid':901})
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)

    def test_get_event_list_eid_success(self):
        ''' 根据 eid 查询结果成功 '''
        r = requests.get(self.baseurl, params={'eid': 3})
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        # self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data']['name'], u'红米MAX发布会')
        self.assertEqual(self.result['data']['address'], u'北京会展中心')

if __name__ == '__main__':
    unittest.main()