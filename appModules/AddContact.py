from pageObjects.HomePage import HomePage
from pageObjects.NewContact import AddContactPage


class NewContactPersonAction(object):
    def __init__(self):
        pass

    @staticmethod
    def addContact(driver, contactName, contactMail, isSatr, contactPhone, contactComment):
        homePage = HomePage(driver)
        # 点击通讯录
        homePage.addressLink().click()
        # 点击新建联系人
        addContact = AddContactPage(driver)
        addContact.newContact().click()
        if contactName:
            # 非必填项
            addContact.addName().send_keys(contactName)
        # 必填项
        addContact.addMail().send_keys(contactMail)
        if isSatr == '是':
            addContact.markStar().click()
        if contactPhone:
            addContact.addPhone().send_keys(contactPhone)
        if contactComment:
            addContact.addContent().send_keys(contactComment)
        addContact.clickCommitBtn().click()

if __name__=='__main__':
    from appModules.LoginAction import LoginAction
    import time
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('https://mail.126.com')
    time.sleep(5)
    LoginAction.login(driver, 'linuxxiaochao', 'xiaochao11520')
    NewContactPersonAction.addContact(driver, '','123456@qq.com', '是', '','')
    time.sleep(5)
    driver.quit()