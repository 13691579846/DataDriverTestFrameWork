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
import os

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 项目目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_DIR = os.path.join(ROOT_DIR, 'config')
DATA_DIR = os.path.join(ROOT_DIR, 'testData')
# 日志文件存放路径
LOG_DIR = os.path.join(ROOT_DIR, 'log')
# 错误截图路径
IMAGE_DIR = os.path.join(ROOT_DIR, 'img')
# init文件路径
pageElementLocatorPath = os.path.join(CONFIG_DIR, 'PageElementLocator.ini')
# excel文件路径
testExcelValuePath = os.path.join(DATA_DIR, '126MailContact.xlsx')


# 126username 表，每列对用的序号
accountUserName = 2
accountPassWord = 3
accountDataBook = 4
accountIsExecute = 5
accountTestResult = 6

# 126联系人表，每列对应的序号
contactName = 2
contactMail = 3
contactStar = 4
contactPhone = 5
contactComment = 6
contactKeyWords = 7
contactIsExecute = 8
contactExecuteTime = 9
contactTestResult = 10


if __name__ == '__main__':
    print(pageElementLocatorPath)
    print(testExcelValuePath)
    print(LOG_DIR)
