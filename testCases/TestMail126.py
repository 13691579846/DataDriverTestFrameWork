from selenium import webdriver
import time
from appModules.LoginAction import LoginAction
from appModules.AddContact import NewContactPersonAction
from config.varCondig import *
from util.ParseExcel import ParseExcel

p = ParseExcel()
sheetName = p.wb.sheetnames # 获取所有的sheetname 是个列表
# print(sheetName)
def bDriver():
    try:
        driver = webdriver.Firefox()
        driver.get('https://mail.126.com')
        driver.implicitly_wait(30)
    except Exception as e:
        raise e
    else:
        return driver

def testMailLogin():
    '''
    测试用例
    :return:
    '''
    # 是否执行列数据
    isExcute = p.getColumnValue(sheetName=sheetName[0], colNo=account_isExecute)
    # print(isExcute)
    for idx,value in enumerate(isExcute[:]):
        # print(idx, value) # 获取是否执行列数据列表的索引和数据
        if value.lower() == 'y':
            userRowValue = p.getRowValue(sheetName[0], idx+2) # 获取执行状态为y所在行的数据
            userName = userRowValue[account_userName-2]
            passWord = userRowValue[account_passWord-2]
            driver = bDriver()
            LoginAction.login(driver,userName, passWord)
            time.sleep(5)
            driver.quit()
    # try:
    #     driver = webdriver.Firefox()
    #     driver.get('https://mail.126.com')
    #     driver.implicitly_wait(30)
    #     LoginAction.login(driver, 'linuxxiaochao', 'xiaochao11520')
    #     time.sleep(5)
    #     assert '未读邮件' in driver.page_source
    # except Exception as e:
    #     raise e
    # finally:
    #     driver.quit()

if __name__=='__main__':
    testMailLogin()
