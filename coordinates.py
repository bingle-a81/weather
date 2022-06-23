import logging.config

from urllib3 import Retry
from settings import logger_config


# from typing import Union
# from typing import Literal
# from dataclasses import dataclass

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')

def func(ro: dict)-> int:
    try:
        s=sum(ro)
        return s
    except Exception as e:
        logger.info(e, exc_info=True)

def a(d:int)->int:
    try:
        return d+10
    except TypeError as e:
        logger.info(f'warning!{e}') 
        # logger.exception(e)
    

def main():
    # logger.debug(r'console')
    # logger.info(r'console file')    
    # logger.warning(r'console file telegram')
    # logger.error(r'console file telegram mail')

    d=a('10')
    print(d)
    dict1=[]
    for i in range(10):
        dict1.append(i)
    f=func(10)
    logger.debug(f)



if __name__ == '__main__':
    main()
