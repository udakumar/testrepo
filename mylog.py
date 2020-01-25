import logging

logging.basicConfig(level=logging.INFO, filename='div.log', filemode='a',\
                    format='%(asctime)s- %(lineno)d-%(levelname)s-%(message)s-%(funcName)s')
logger = logging.getLogger()