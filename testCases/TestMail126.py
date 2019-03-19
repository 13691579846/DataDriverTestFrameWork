from selenium import webdriver
import time
from appModules.LoginAction import LoginAction
def testMailLogin():
    '''
    测试用例
    :return:
    '''
    try:
        driver = webdriver.Firefox()
        driver.get('https://mail.126.com')
        driver.implicitly_wait(30)
        LoginAction.login(driver, 'linuxxiaochao', 'xiaochao11520')
        time.sleep(5)
        assert '未读邮件' in driver.page_source
    except Exception as e:
        raise e
    finally:
        driver.quit()

if __name__=='__main__':
    testMailLogin()
