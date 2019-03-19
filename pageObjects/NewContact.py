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

