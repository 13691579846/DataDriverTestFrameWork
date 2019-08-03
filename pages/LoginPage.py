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


class LoginPage(Base):
    """登录页面所有的操作元素对象"""

    cf = DoConf()

    @property
    def click_password_login_btn(self):
        by, locator = self.cf.get_element_value('126mail_login', 'loginPage.passWordLoginBtn')
        password_login_btn = self.get_element(by, locator)
        return password_login_btn

    def switch_to_frame(self):
        """切换frame"""
        by, locator = self.cf.get_element_value('126mail_login', 'loginPage.frame')
        try:
            self.switch_frame(by, locator)
        except Exception as e:
            raise e

    def switch_to_default_frame(self):
        """跳出frame"""
        try:
            self.switch_to_default()
        except Exception as e:
            raise e

    @property
    def user_name_element(self):  # 用户名输入框
        by, locator = self.cf.get_element_value('126mail_login', 'loginPage.username')
        username = self.get_element(by, locator)
        return username

    @property
    def password_element(self):  # 密码输入框
        by, locator = self.cf.get_element_value('126mail_login', 'loginPage.password')
        password = self.get_element(by, locator)
        return password

    @property
    def login_btn_element(self):  # 登录按钮
        by, locator = self.cf.get_element_value('126mail_login', 'loginPage.loginBtn')
        login_btn = self.get_element(by, locator)
        return login_btn


if __name__ == '__main__':
    pass
