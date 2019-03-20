# 封装登录方法

from pageObjects.LoginPage import LoginPage
class LoginAction(object):
    def __init__(self):
        pass

    @staticmethod #
    def login(driver, username, password):
        login = LoginPage(driver)
        login.switchToFrame()
        login.userNameObj().send_keys(username)
        login.passwordObj().send_keys(password)
        login.loginBtnObj().click()
        login.switchToDefaultFrame()

if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('https://mail.126.com')
    LoginAction.login(driver, 'linuxxiaochao', 'xiaochao11520')