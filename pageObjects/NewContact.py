from util.ParseConfigurationFile import ParseConfigFile
from util.ObjectMap import *

class AddContactPage(object):
    '''
    添加联系人页面所有操作元素对象
    '''
    def __init__(self, driver):
        self.driver = driver
        self.cf = ParseConfigFile()

    def newContact(self): # 新建联系人
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newContact')

        element = getElement(self.driver, by, locator)
        return element

    def addName(self): # 姓名输入框
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newName')

        element = getElement(self.driver, by, locator)
        return element

    def addMail(self): # 电子邮件输入框
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newMail')

        element = getElement(self.driver, by, locator)
        return element

    def markStar(self): # 设为星际联系人
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newMark')

        element = getElement(self.driver, by, locator)
        return element

    def addPhone(self): # 手机号码输入框
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newPhone')

        element = getElement(self.driver, by, locator)
        return element

    def addContent(self): # 备注
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newComment')

        element = getElement(self.driver, by, locator)
        return element

    def clickCommitBtn(self): # 确定按钮
        by, locator = self.cf.getElementValue('126mail_addContactPage', 'addContactPage.newCommit')

        element = getElement(self.driver, by, locator)
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
    LoginAction.login(driver,'linux', 'chao')
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