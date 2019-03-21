import os

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 项目目录
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# init文件路径
pageElementLocatorPath = parentDirPath+r'\config\PageElementLocator.ini'
# excel文件路径
testExcelValuePath = parentDirPath+r'\testData\126MailContact.xlsx'
# 日志文件存放路径
logPath = parentDirPath + r'\log'

# 126username 表，每列对用的序号
account_userName = 2
account_passWord = 3
account_dataBook = 4
account_isExecute = 5
account_testResult = 6

# 126联系人表，每列对应的序号
contact_contactName = 2
contact_contactMail = 3
contact_contactStar = 4
contact_contactPhone = 5
contact_contactComment = 6
contact_contactKeyWords = 7
contact_contactIsExcute = 8
contact_contactExcuteTime = 9
contact_contactTestResult = 10

if __name__=='__main__':

    print(pageElementLocatorPath)
    print(testExcelValuePath)
    print(logPath)