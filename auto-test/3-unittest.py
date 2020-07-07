from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class TestSearchResult(unittest.TestCase):
    def testsearch(self):
        driver = webdriver.Chrome(r'd:\chromedriver.exe')
        driver.get("https://www.51job.com")
        elem = driver.find_element_by_id("kwdselectid")
        elem.send_keys("python")
        elem = driver.find_element_by_css_selector('.ush button')
        elem.click()

        elems = driver.find_elements_by_css_selector('#resultList div[class=el]')
        data = []
        cnt = 0
        for elem in elems:
            line = elem.find_elements_by_tag_name('span')
            t = [i.text for i in line]
            # check title has key words : python
            title = t[0]
            if 'python' in t[0] or 'Python' in t[0]:
                cnt += 1
            print(t)
            data.append(t)
        self.assertTrue(cnt/len(data) > 0.6, 'keywords ratio: '+str(cnt/len(data) ))

if __name__ == '__main__':
    unittest.main()

