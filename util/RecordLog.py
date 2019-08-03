import logging
import time

from config.config import LOG_DIR


class Logger(object):
    """封装的日志模块"""
    def __init__(self, logger, file_level=logging.INFO):
        """
        :param logger: logger名
        :param file_level: 文件级别
        """
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # 设置日志输出的默认级别
        # 日志输出格式
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        # 日志文件名称
        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = LOG_DIR + r'/' + 'log' + curr_time + '.txt'
        # 设置文件输出
        fh = logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(file_level)  # 日志级别
        self.logger.addHandler(fh)


if __name__ == '__main__':
    log = Logger("fox", file_level=logging.DEBUG)
    log.logger.debug("debug")
    log.logger.log(logging.ERROR, '%(module)s %(info)s', {'module': 'log日志', 'info': 'error'})
