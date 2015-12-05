# -*- coding: utf-8 -*-

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s:%(msecs)05.1f pid:%(process)d [%(levelname)s] (%(funcName)s) %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='pg_insert.log',
    filemode='a+')
logger = logging.getLogger()
