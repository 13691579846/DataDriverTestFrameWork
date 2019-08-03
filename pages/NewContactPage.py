"""
------------------------------------
@Time : 2019/8/3 21:59
@Auth : linux超
@File : GetDateTime.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException

from util.ParseConfig import ParseConfigFile as DoConf
from pages.base import Base


class AddContactPage(Base):
    """添加联系人页面所有操作元素对象"""
    cf = DoConf()

    @property
    def wait_new_contact_visibility(self):
        by, locator = self.cf.get_element_value('126mail_addContactPage', 'addContactPage.newContact')
        try:
            return WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((by, locator)))
        except TimeoutException:
            print("新键联系人按钮不可以点击或者没有找到")

    @property
    def new_contact(self):  # 新建联系人
        # by, locator = self.cf.get_element_value('126mail_addContactPage', 'addContactPage.newContact')
        element = self.wait_new_contact_visibility
        return element

    @property
    def add_name(self):  # 姓名输入框
        by, locator = self.cf.get_element_value('126mail_addContactPage', 'addContactPage.newName')
        element = self.get_element(by, locator)
        return element

    @property
    def add_mail(self):  # 电子邮件输入框
        by, locator = self.cf.get_element_value('126mail_addContactPage', 'addContactPage.newMail')
        element = self.get_element(by, locator)
        return element

    @property
    def mark_star(self):  # 设为星际联系人
        by, locator = self.cf.get_element_value('126mail_addContactPage', 'addContactPage.newMark')
        element = self.get_element(by, locator)
        return element

    @property
    def add_phone(self):  # 手机号码输入框
        by, locator = self.cf.get_element_value('126mail_addContactPage', 'addContactPage.newPhone')
        element = self.get_element(by, locator)
        return element

    @property
    def add_content(self):  # 备注
        by, locator = self.cf.get_element_value('126mail_addContactPage', 'addContactPage.newComment')
        element = self.get_element(by, locator)
        return element

    @property
    def click_commit_btn(self):  # 确定按钮
        by, locator = self.cf.get_element_value('126mail_addContactPage', 'addContactPage.newCommit')
        element = self.get_element(by, locator)
        return element


if __name__ == '__main__':
    pass
