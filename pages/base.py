from selenium.webdriver.support.wait import WebDriverWait

from util.GetDateTime import DateTime as DataTime


class Base(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30)
        self.url = 'https://mail.126.com'

    def open_url(self):
        return self.driver.get(self.url)

    def delete_cookies(self):
        return self.driver.delete_all_cookies()

    def get_element(self, by, locate):
        """
        查找单一个元素
        :param by: 定位方式，id, name, class, xpath...
        :param locate: 定位表达式
        :return: 元素
        """
        try:
            element = WebDriverWait(self.driver, 30).until(lambda x: x.find_element(by, locate))
        except Exception as e:
            raise e
        else:
            return element

    def get_elements(self, by, locate):
        """
        查找一组元素
        :param by: 定位方式
        :param locate: 定位表达式
        :return: 一组元祖组成的列表
        """
        try:
            elements = WebDriverWait(self.driver, 30).until(lambda x: x.find_elements(by, locate))
        except Exception as e:
            raise e
        else:
            return elements

    def save_screen_shot(self, string):
        picture_name = \
            DataTime.create_picture_path() + '\\' + DataTime.get_current_time() + string + '.png'
        try:
            self.driver.get_screenshot_as_file(picture_name)
        except Exception as e:
            raise e
        else:
            return picture_name

    def switch_frame(self, by, locator):
        iframe = self.get_element(by, locator)
        return self.driver.switch_to.frame(iframe)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def quit(self):
        return self.driver.quit()


if __name__ == '__main__':
    pass
