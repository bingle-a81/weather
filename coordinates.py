import logging.config
from settings import logger_config


# from typing import Union
# from typing import Literal
# from dataclasses import dataclass

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')


def main():
    logger.debug(r'это консоль')
    logger.info(r'это консоль и файл')
    logger.warning(r'это консоль файл телега')
    logger.error(r'это консоль файл телега мыло')
    print(10 + 15)


if __name__ == '__main__':
    main()
