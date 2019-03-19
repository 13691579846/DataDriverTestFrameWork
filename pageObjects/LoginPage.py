from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
class LoginPage(object):
    '''
    保存登录页面元素
    '''
    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile()

    def switchToFrame(self):
        by, locator = self.cf.getElementValue('126mail_login', 'loginPage.frame')
        self.driver.switch_to.frame(getElement(self.driver, by,locator))

    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()

    def userNameObj(self):
        by, locator = self.cf.getElementValue('126mail_login', 'loginPage.username')
        try:
            username = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return username

    def passwordObj(self):
        by, locator = self.cf.getElementValue('126mail_login', 'loginPage.password')
        try:
            password = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return password

    def loginBtnObj(self):
        by, locator = self.cf.getElementValue('126mail_login', 'loginPage.loginBtn')
        try:
            loginbtn = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return loginbtn

if __name__=='__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Firefox()
    driver.get('https://mail.126.com')
    login = LoginPage(driver)
    time.sleep(5)
    login.switchToFrame()
    login.userNameObj().send_keys('linuxxiaochao')
    login.passwordObj().send_keys('xiaochao11520')
    login.loginBtnObj().click()
    login.switchToDefaultFrame()
    driver.quit()
