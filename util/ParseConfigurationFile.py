from config.varCondig import pageElementLocatorPath
import configparser

class ParseConfigFile(object):
    '''
    解析ini配置文件
    '''
    def __init__(self):
        try:
            self.cf = configparser.ConfigParser() # 获取配置文件对象
            self.cf.read(pageElementLocatorPath, encoding='utf-8') # 加载配置文件到内存中
        except Exception as e:
            raise e

    def getItemsSection(self, sectionName):
        '''
        获取section下面所有section的键值
        :param sectionName:
        :return:
        '''
        try:
            vlaues = dict(self.cf.items(sectionName))
        except Exception as e:
            raise e
        else:
            return vlaues

    def getElementValue(self, sectionName, optionName):
        try:
            locator = self.cf.get(sectionName, optionName).split('>')
        except Exception as e:
            raise e
        else:
            return locator # 获取option键对应的value

    def getAllSections(self):
        try:
            allsections = self.cf.sections()
        except Exception as e:
            raise e
        else:
            return allsections # 所有的sections返回值是个列表

    def getAllOptions(self, section):
        try:
            options = self.cf.options(section)
        except Exception as e:
            raise e
        else:
            return options # 某个section下面的键

if __name__=='__main__':
    cf = ParseConfigFile()
    locator = cf.getElementValue('126mail_login','loginPage.username')
    # print(locator)
    print(cf.getItemsSection('126mail_login'))
    print(cf.getAllSections())
    print(cf.getAllOptions('126mail_addContactPage'))