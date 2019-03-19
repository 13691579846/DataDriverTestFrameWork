from util.ObjectMap import *

class LoginPage(object):
    '''
    保存登录页面元素
    '''
    def __init__(self, driver):
        self.driver = driver

    def switchToFrame(self):

        self.driver.switch_to.frame(getElement(self.driver, 'xpath', "//div[@id='loginDiv']/iframe"))
    def switchToDefaultFrame(self):
        self.driver.switch_to.default_content()
    def userNameObj(self):
        try:
            username = getElement(self.driver, "xpath", "//input[@name='email']")
        except Exception as e:
            raise e
        else:
            return username
    def passwordObj(self):
        try:
            password = getElement(self.driver, "xpath", "//input[@name='password']")
        except Exception as e:
            raise e
        else:
            return password
    def loginBtnObj(self):
        try:
            loginbtn = getElement(self.driver, "xpath", "//a[@id='dologin']")
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
