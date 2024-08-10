import os
import sys

from loguru import logger

current_file_path = os.path.abspath(__file__)
project_path = os.path.dirname(os.path.dirname(current_file_path))


class LogUtil:
    def __init__(self, tag='log', log_file_name='running.log'):
        # """
        # log记录模块
        # :param tag: 标签，用于区分log
        # :param log_file_name: log名称，默认Vulcan.log
        # """
        # # 1.仅仅记录log，并将log的内容以print的方式输出到控制台(默认配色)
        logger.configure(handlers=[{
            "sink": f'{project_path}/logs/{str(log_file_name).rstrip(".log")}-' +
                    '{time:YYYY-MM-DD}.log',
            "rotation": '28 MB',
            "retention": '1 days',
            "compression": 'zip'
        }])
        logger.add(sys.stdout,
                   format='{time:YYYY-MM-DD HH:mm:ss} | {level:<7} | {thread.name} | {module}:{line} | - {message}',
                   filter=lambda record: record['extra'].get('name') == tag, level='DEBUG')

        # # 2.记录log，并以更加美观的方式将log输出到控制台
        # logger.add(f'{project_path}/logs/{str(log_file_name).rstrip(".log")}-' + '{time:YYYY-MM-DD}.log',
        #            format='{time:YYYY-MM-DD HH:mm:ss} | {level:<7} | {module}:{line} - {message}',
        #            filter=lambda record: record['extra'].get('name') == tag, level='DEBUG', rotation='16 MB',
        #            retention='1 days', compression='zip')
        self.logger = logger.bind(name=tag)

    def get_logger(self):
        return self.logger
