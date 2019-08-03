from pages.LoginPage import LoginPage


class LoginAction(object):

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def click_password_login(self):
        self.login_page.click_password_login_btn.click()

    def login(self, username, password):
        """登录场景"""
        self.login_page.switch_to_frame()
        self.login_page.user_name_element.send_keys(username)
        self.login_page.password_element.send_keys(password)
        self.login_page.login_btn_element.click()
        self.login_page.switch_to_default_frame()


if __name__ == '__main__':
    pass
