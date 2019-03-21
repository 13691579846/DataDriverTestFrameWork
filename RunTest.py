'''
用例执行入口
'''

import sys
sys.path.append(r'.')

if __name__=='__main__':
    from testCases.TestMail126 import *

    driver = bDriver()
    testMailLogin(driver)