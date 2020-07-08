class IndexPage():
    def __init__(self, driver):
        self.driver = driver
        driver.get("https://www.mi.com/")

    def to_login(self):
        self.driver.find_element_by_xpath("//div[@id='J_siteUserInfo']/a[1]").click()
        self.driver.find_element_by_xpath("//div[@id='J_siteUserInfo']/a[1]").click()
        ffs = self.driver.find_elements_by_xpath("//*[@class='btn btn-primary']")
        if len(ffs) != 0:
            ffs[0].click()
        return LoginPage(self.driver)

    def search_item(self, item):
        self.driver.find_element_by_id('search').send_keys(item)
        return GoodItemsPage(self.driver)



class LoginPage():
    def __index__(self, driver):
        self.driver = driver
    def login(self, usrname, password):
        self.driver.find_element_by_id("username").send_keys('2423963832')
        self.driver.find_element_by_id("pwd").send_keys('sqtest_123')
        self.driver.find_element_by_id('login-button').click()
        return IndexPage(self.driver)

class GoodItemsPage():
    def __index__(self, driver):
        self.driver = driver

    def pick_item(self):
        driver.find_element_by_css_selector(".sale_btn>a").click()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if '小米10系列购买--小米商城' == self.driver.title:
                print('ok!')
                return ItemPage(self.driver)


class ItemPage():
    def __init__(self, driver):
        self.driver = driver
    def add_to_cart(self):
        driver.find_element_by_css_selector(".sale_btn>a").click()
        return CartPage(self.driver)
class CartPage():
    def __init__(self, driver):
        self.driver = driver

    def check(self):
        res = self.driver.find_element_by_class_name('good-info').text
        assert '小米10' in res

if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome(r'd:\chromedriver.exe')
    IndexPage(driver).to_login().login('2423963832', 'sqtest_123').\
        search_item('小米10\n').pick_item().add_to_cart()
    driver.quit()

