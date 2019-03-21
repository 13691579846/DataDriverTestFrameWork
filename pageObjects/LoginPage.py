from util.ObjectMap import *
from util.ParseConfigurationFile import ParseConfigFile
class LoginPage(object):
    '''
    登录页面所有的操作元素对象
    '''
    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile()

    def switchToFrame(self):
        '''
        切换到frame中
        :return:
        '''
        by, locator = self.cf.getElementValue('126mail_login', 'loginPage.frame')
        try:
            self.driver.switch_to.frame(getElement(self.driver, by,locator))
        except Exception as e:
            raise e

    def switchToDefaultFrame(self):
        '''
        跳出frame
        :return:
        '''
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            raise e

    def userNameObj(self): # 用户名输入框
        by, locator = self.cf.getElementValue('126mail_login', 'loginPage.username')

        username = getElement(self.driver, by, locator)
        return username

    def passwordObj(self): # 密码输入框
        by, locator = self.cf.getElementValue('126mail_login', 'loginPage.password')

        password = getElement(self.driver, by, locator)
        return password

    def loginBtnObj(self): # 登录按钮
        by, locator = self.cf.getElementValue('126mail_login', 'loginPage.loginBtn')

        loginbtn = getElement(self.driver, by, locator)
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
