import requests
import unittest
class GetEventListTest(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://127.0.0.1:8000/api/get_event_list/'
    def test_get_event_null(self):
        """发布会id为空"""
        r = requests.get(self.url, params={'eid':''})
        result = r.json()
        self.assertEqual(result['status'], 10022)

    def test_get_event_error(self):
        """发布会id不存在"""
        r = requests.get(self.url, params={'eid': '901'})
        result = r.json()
        self.assertEqual(result['status'], 10022)

    def test_get_event_success(self):
        """发布会id正确"""
        r = requests.get(self.url, params={'eid': '3'})
        result = r.json()
        self.assertEqual(result['status'], 200)

if __name__ == '__main__':
    unittest.main()
    
