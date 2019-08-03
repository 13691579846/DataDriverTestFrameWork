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
from config.config import pageElementLocatorPath as UiObjectLibrary
import configparser


class ParseConfigFile(object):
    """解析ini配置文件"""

    def __init__(self):
        try:
            self.cf = configparser.ConfigParser()  # 获取配置文件对象
            self.cf.read(UiObjectLibrary, encoding='utf-8')  # 加载配置文件到内存中
        except Exception as e:
            raise e

    def get_items_section(self, section_name):
        """
        获取section下面所有section的键值
        :param section_name:
        :return:
        """
        try:
            values = dict(self.cf.items(section_name))
        except Exception as e:
            raise e
        else:
            return values

    def get_element_value(self, section_name, option_name):
        try:
            locator = self.cf.get(section_name, option_name).split('>')
        except Exception as e:
            raise e
        else:
            return locator  # 获取option键对应的value

    def get_all_sections(self):
        try:
            all_sections = self.cf.sections()
        except Exception as e:
            raise e
        else:
            return all_sections  # 所有的sections返回值是个列表

    def get_all_options(self, section):
        try:
            options = self.cf.options(section)
        except Exception as e:
            raise e
        else:
            return options  # 某个section下面的键


if __name__ == '__main__':
    cf = ParseConfigFile()
    location = cf.get_element_value('126mail_login', 'loginPage.username')
    print(cf.get_items_section('126mail_login'))
    print(cf.get_all_sections())
    print(cf.get_all_options('126mail_addContactPage'))
