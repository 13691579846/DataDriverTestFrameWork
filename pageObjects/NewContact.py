from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *

class AddContactPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile()

    def newContact(self):
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newContact')
        try:
            element = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return element

    def addName(self):
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newName')
        try:
            element = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return element

    def addMail(self):
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newMail')
        try:
            element = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return element

    def markStar(self):
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newMark')
        try:
            element = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return element

    def addPhone(self):
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newPhone')
        try:
            element = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return element

    def addContent(self):
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newComment')
        try:
            element = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return element

    def clickCommitBtn(self):
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newCommit')
        try:
            element = getElement(self.driver, by, locator)
        except Exception as e:
            raise e
        else:
            return element

if __name__=='__main__':
    from selenium import webdriver
    import time
    from pageObjects.HomePage import HomePage
    from appModules.LoginAction import LoginAction

    driver = webdriver.Firefox()
    driver.get('https://mail.126.com')
    time.sleep(3)
    # 登录
    LoginAction.login(driver,'linuxxiaochao', 'xiaochao11520')
    # 主页面
    homepage = HomePage(driver)
    homepage.addressLink().click()
    time.sleep(5)
    # 添加联系人页面
    addcontact = AddContactPage(driver)
    addcontact.newContact().click()
    time.sleep(2)
    addcontact.addName().send_keys('test')
    addcontact.addMail().send_keys('13691579846@qq.com')
    addcontact.addPhone().send_keys('13691579846')
    addcontact.addContent().send_keys('ceshi')
    addcontact.markStar().click()
    time.sleep(3)
    addcontact.clickCommitBtn().click()