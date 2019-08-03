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
