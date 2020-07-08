from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'd:\chromedriver.exe')
driver.get("https://www.mi.com/")

# login
driver.find_element_by_xpath("//div[@id='J_siteUserInfo']/a[1]").click()
ffs = driver.find_elements_by_xpath("//*[@class='btn btn-primary']")
if len(ffs) != 0:
    ffs[0].click()

driver.find_element_by_id("username").send_keys('2423963832')
driver.find_element_by_id("pwd").send_keys('sqtest_123')
driver.find_element_by_id('login-button').click()

# search

driver.find_element_by_id('search').send_keys('小米10\n')
driver.find_element_by_css_selector(".sale_btn>a").click()
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if '小米10系列购买--小米商城' == self.driver.title:
        print('ok!')
        break



res = driver.find_element_by_class_name('good-info').text

driver.quit()









