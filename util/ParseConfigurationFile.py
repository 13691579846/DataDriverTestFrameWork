from config.varCondig import pageElementLocatorPath
import configparser

class ParseConfigFile(object):
    '''
    解析配置文件
    '''
    def __init__(self):
        self.cf = configparser.ConfigParser() # 获取配置文件对象
        self.cf.read(pageElementLocatorPath, encoding='utf-8') # 加载配置文件到内存中

    def getItemsSection(self, sectionName):
        vlaues = dict(self.cf.items(sectionName))
        return vlaues

    def getElementValue(self, sectionName, optionName):
        locator = self.cf.get(sectionName, optionName).split('>')
        return locator # 获取option键对应的value

    def getAllSections(self):
        allsections = self.cf.sections()
        return allsections # 所有的sections返回值是个列表

    def getAllOptions(self, section):
        section = self.cf.options(section)
        return section # 某个section下面的键

if __name__=='__main__':
    cf = ParseConfigFile()
    locator = cf.getElementValue('126mail_login','loginPage.username')
    # print(locator)
    print(cf.getItemsSection('126mail_login'))
    print(cf.getAllSections())
    print(cf.getAllOptions('126mail_addContactPage'))