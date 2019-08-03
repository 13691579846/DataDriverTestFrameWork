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
import time
import logging
import traceback
from selenium import webdriver

from bussines.LoginAction import LoginAction as LoginAction
from bussines.AddContact import NewContactPersonAction as NewAction
from config.config import (
    accountIsExecute as accountIsExecute,
    accountUserName as accountUserName,
    accountPassWord as accountPassWord,
    accountDataBook as accountDataBook,
    accountTestResult as accountTestResult,
    contactIsExecute as contactIsExecute,
    contactName as contactName,
    contactMail as contactMail,
    contactStar as contactStar,
    contactPhone as contactPhone,
    contactComment as contactComment,
    contactKeyWords as contactKeyWords,
    contactTestResult as contactTestResult
)
from util.ParseExcel import ParseExcel
from util.RecordLog import Logger
from pages.base import Base


log = Logger(__name__, logging.INFO)
do_excel = ParseExcel()
sheetName = do_excel.wb.sheetnames  # 获取所有的sheetname 是个列表


def test_mail_login():
    """测试用例"""
    driver = webdriver.Firefox()
    base = Base(driver)
    base.open_url()
    login_action = LoginAction(driver)
    add_contact = NewAction(driver)
    # 是否执行列数据
    is_execute = do_excel.get_column_value(sheetName[0], accountIsExecute)
    data_book = do_excel.get_column_value(sheetName[0], accountDataBook)
    for idx, value in enumerate(is_execute[:]):
        # print(idx, value) # 获取是否执行列数据列表的索引和数据
        if value.lower() == 'y':
            user_row_value = do_excel.get_row_value(sheetName[0], idx + 2)  # 获取执行状态为y所在行的数据
            user_name = user_row_value[accountUserName - 2]
            pass_word = user_row_value[accountPassWord - 2]
            # 登录
            login_action.click_password_login()
            login_action.login(user_name, pass_word)
            time.sleep(10)  # 足够的时间加载登录成功的页面
            try:
                assert '通讯录' in driver.page_source
            except Exception:
                base.save_screen_shot(user_name + '-' + pass_word + '失败')
                log.logger.info('登录失败,输出信息如下：{}'.format(traceback.format_exc()))
                do_excel.write_cell(sheetName[0], idx + 2, accountTestResult, 'failed')
                base.delete_cookies()
                base.open_url()
            else:
                log.logger.info('账号：{}登录成功, 测试通过'.format(user_name))
                do_excel.write_cell(sheetName[0], idx + 2, accountTestResult, 'pass')
                # 获取联系人数据表中是否执行列的数据
                if data_book[idx] == sheetName[1]:
                    is_execute = do_excel.get_column_value(sheetName[1], contactIsExecute)
                    for index, data in enumerate(is_execute):
                        if data.lower() == 'y':
                            # 获取y表示行的数据
                            contact_person_value = \
                                do_excel.get_row_value(sheetName[1], index + 2)
                            # 获取添加联系人所需的数据
                            # 联系人姓名
                            contact_person_name = \
                                contact_person_value[contactName - 2]
                            # 联系人邮箱
                            contact_person_mail = \
                                contact_person_value[contactMail - 2]
                            # 是否为星级联系人
                            contact_person_star = \
                                contact_person_value[contactStar - 2]
                            # 联系人手机号
                            contact_person_phone = \
                                contact_person_value[contactPhone - 2]
                            # 联系人备注
                            contact_person_comment = \
                                contact_person_value[contactComment - 2]
                            # 验证页面包含的关键字
                            contact_assert = \
                                contact_person_value[contactKeyWords - 2]
                            add_contact.address_link()
                            add_contact.add_contact(
                                contact_person_name,
                                contact_person_mail,
                                contact_person_star,
                                contact_person_phone,
                                contact_person_comment
                            )
                            try:
                                assert contact_assert in driver.page_source
                            except Exception:
                                base.save_screen_shot('添加联系人失败')
                                do_excel.write_cell(sheetName[1], index + 2, contactTestResult, 'fail')
                            else:
                                do_excel.write_cell(sheetName[1], index + 2, contactTestResult, 'pass')
                            # 设置足够长的时间 让添加联系人成功后的提示框自动消失，当然可以自己写代码关闭
                            time.sleep(10)
                    base.delete_cookies()
                    base.open_url()
                else:
                    base.delete_cookies()
                    base.open_url()
    base.quit()


if __name__ == '__main__':
    pass
