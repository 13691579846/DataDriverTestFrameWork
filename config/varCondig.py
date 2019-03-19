import os

# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pageElementLocatorPath = parentDirPath+r'\config\PageElementLocator.ini'
if __name__=='__main__':

    print(pageElementLocatorPath)