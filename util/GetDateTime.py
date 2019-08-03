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
from datetime import datetime, date

from config.config import IMAGE_DIR as IMG


class DateTime(object):

    @staticmethod
    def get_current_date():
        """获取当前日期"""
        try:
            current_date = date.today()
        except Exception as e:
            raise e
        else:
            return str(current_date)

    @staticmethod
    def get_current_time():
        """获取当前时间"""
        try:
            time = datetime.now()
            current_time = time.strftime('%H_%M_%S')
        except Exception as e:
            raise e
        else:
            return current_time

    @staticmethod
    def create_picture_path():
        """创建图片存放路径路径"""
        try:
            picture_path = os.path.join(IMG, DateTime.get_current_date())
            if not os.path.exists(picture_path):
                os.makedirs(picture_path)  # 生成多级目录
        except Exception as e:
            raise e
        else:
            return picture_path


if __name__ == '__main__':
    print(DateTime.get_current_date())
    print(DateTime.get_current_time())
    print(DateTime.create_picture_path())
