from selenium.webdriver.support.wait import WebDriverWait

def getElement(driver, by, locate):
    '''
    查找单一个元素
    :param driver: 浏览器驱动
    :param by: 定位方式，id, name, class, xpath...
    :param locate: 定位表达式
    :return: 元素
    '''
    try:
        element = WebDriverWait(driver, 30).until(lambda x :x.find_element(by, locate))
    except Exception as e:
        raise e
    else:
        return element
def getElelments(driver, by, locate):
    '''
    查找一组元素
    :param driver: 浏览器驱动
    :param by: 定位方式
    :param locate: 定位表达式
    :return: 一组元祖组成的列表
    '''
    try:
        elements = WebDriverWait(driver, 30).until(lambda x :x.find_elements(by, locate))
    except Exception as e:
        raise e
    else:
        return elements
if __name__=='__main__':
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.get('http://www.baidu.com')
    inputBaidu = getElement(driver, 'id', 'kw')
    inputBaidu.send_keys('python')
