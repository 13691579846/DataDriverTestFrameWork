from selenium import webdriver
import time
from appModules.LoginAction import LoginAction
from appModules.AddContact import NewContactPersonAction
from config.varCondig import *
from util.ParseExcel import ParseExcel
from util.Log import Logger
import logging
import traceback

log = Logger(__name__, CmdLevel=logging.INFO, FileLevel=logging.INFO)
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

def testMailLogin(driver):
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
            # driver = bDriver()
            # 登录
            LoginAction.login(driver,userName, passWord)
            time.sleep(10) # 足够的时间加载登录成功的页面
            try:
                assert '通讯录' in driver.page_source
            except Exception as e:
                log.logger.info('断言"通讯录"失败,错误信息{}'.format(traceback.format_exc()))
                p.writeCell(sheetName[0], idx + 2, account_testResult, 'failed')
                # raise e
            else:
                log.logger.info('{},{}登录成功, 断言”通讯录“成功'.format(userName, passWord))
                p.writeCell(sheetName[0], idx + 2, account_testResult, 'pass')
            # 获取联系人数据表中是否执行列的数据
                isExcute = p.getColumnValue(sheetName=sheetName[1], colNo=contact_contactIsExcute)
                for idx, value in enumerate(isExcute):
                    if value.lower() == 'y':
                        # 获取y表示行的数据
                        contactPersonValue = p.getRowValue(sheetName[1], idx+2)
                        # 获取添加联系人所需的数据
                        # 联系人姓名
                        contactPersonName = contactPersonValue[contact_contactName-2]
                        # 联系人邮箱
                        contactPersonMail = contactPersonValue[contact_contactMail-2]
                        # 是否为星级联系人
                        contactPersonStar = contactPersonValue[contact_contactStar-2]
                        # 联系人手机号
                        contactPersonPhone = contactPersonValue[contact_contactPhone-2]
                        # 联系人备注
                        contactPersonComment = contactPersonValue[contact_contactComment-2]
                        # 验证页面包含的关键字
                        contactAssert = contactPersonValue[contact_contactKeyWords-2]
                        NewContactPersonAction.addressLink(driver)
                        NewContactPersonAction.addContact(driver, contactPersonName, contactPersonMail
                                                          , contactPersonStar, contactPersonPhone, contactPersonComment)
                        try:
                            assert contactAssert in driver.page_source
                        except Exception as e:
                            p.writeCell(sheetName[1], idx + 2, contact_contactTestResult, 'failed')
                            raise e
                        else:
                            p.writeCell(sheetName[1], idx+2, contact_contactTestResult, 'pass')
                        # 设置足够长的时间 让添加联系人成功后的提示框自动消失，当然可以自己写代码关闭
                        time.sleep(10)
            driver.quit()

if __name__=='__main__':
    driver = bDriver()
    testMailLogin(driver)
