import unittest, time, ddt
from selenium import webdriver
from utils.excel_read import ParseExcel

path = './../data/test.xls'

@ddt.ddt
class Test_baidu_search(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(r'd:\chromedriver.exe')
    @classmethod
    def tearDown(self) -> None:
        self.driver.quit()
    def setUp(self):
        self.driver.get('http://www.baidu.com/')
    def tearDown(self):
        pass
    @ddt.data(* ParseExcel(path).getDataFromSheetMul())
    def test_search(self, data):
        """search words %s""" %data[1]
        data = data[0]
        self.driver.find_element_by_id('kw').send_keys(data)
        time.sleep(2)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)
        print(self.driver.title)
        self.assertTrue(data in self.driver.title)
if __name__ == '__main__':
    unittest.main()


