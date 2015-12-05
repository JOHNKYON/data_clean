# -*- coding: utf-8 -*-

from __future__ import absolute_import

import codecs
import csv
import psycopg2
import logger

input_file1 = codecs.open('./utf8/edu_without_dup.txt', 'rb')
input_file2 = codecs.open('./utf8/work_without_dup.txt', 'rb',)

# 建立数据库链接
try:
    connection = psycopg2.connect(database="mydb", user="postgres", password="precure", host="127.0.0.1", port="5432")
except:
    logger.logger('Connecting Failed.')

cursor = connection.cursor()


for line in csv.reader(input_file1, delimiter=str('|')):
    try:
        cursor.execute("""if exits(SELECT * FROM person WHERE id = (%s))
                            UPDATE person set edu_intr """ % (line[2]))
    except:
        print 'Execute Failed'
        logger.logger('Execute Failed.')
