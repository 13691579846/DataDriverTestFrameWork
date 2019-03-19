from util.ObjectMap import * #查找元素的模块
from util.ParseConfigurationFile import ParseConfigFile

class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile()

    def addressLink(self):
        by, locator = self.cf.getElementValue('126mail_homePage','homePage.addressbook')
        try:
            elementObj = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return elementObj

if __name__=='__main__':
    from selenium import webdriver
    from pageObjects.LoginPage import LoginPage
    import time
    driver = webdriver.Firefox()
    driver.get('https://mail.126.com')
    login = LoginPage(driver)
    homePage = HomePage(driver)
    time.sleep(5)
    login.switchToFrame()
    login.userNameObj().send_keys('linuxxiaochao')
    login.passwordObj().send_keys('xiaochao11520')
    login.loginBtnObj().click()
    login.switchToDefaultFrame()
    time.sleep(3)
    homePage.addressLink().click()
    time.sleep(10)
    driver.quit()