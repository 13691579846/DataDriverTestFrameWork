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
from pages.base import Base
from util.ParseConfig import ParseConfigFile as DoConf


class HomePage(Base):

    cf = DoConf()

    @property
    def address_link(self):
        """通讯录菜单对象"""
        by, locator = self.cf.get_element_value('126mail_homePage', 'homePage.addressbook')
        element = self.get_element(by, locator)
        return element


if __name__ == '__main__':
    pass
