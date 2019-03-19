from config.varCondig import pageElementLocatorPath
import configparser

class ParseConfigFile(object):
    '''
    解析配置文件
    '''
    def __init__(self):
        self.cf = configparser.ConfigParser() # 获取配置文件对象
        self.cf.read(pageElementLocatorPath) # 加载配置文件到内存中

    def getElementValue(self, sectionName, optionName):
        locator = self.cf.get(sectionName, optionName).split('>')

        return locator
if __name__=='__main__':
    cf = ParseConfigFile()
    locator = cf.getElementValue('126mail_login','loginPage.username')
    print(locator)