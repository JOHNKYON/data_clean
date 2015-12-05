# -*- coding: utf-8 -*-

from __future__ import absolute_import

import codecs
import csv
import psycopg2
import logger
import string

input_file1 = codecs.open('./utf8/edu_without_dup.txt', 'rb')
input_file2 = codecs.open('./utf8/work_without_dup.txt', 'rb', )

# 建立数据库链接
try:
    connection = psycopg2.connect(database="mydb", user="postgres", password="precure", host="127.0.0.1", port="5432")
except:
    logger.logger.info('Connecting Failed.')

cursor = connection.cursor()

count = 0

'''for line in csv.reader(input_file1, delimiter=str('|')):
    if count == 0:
        count += 1
        continue

    # try:
    if line[9] != '' or line[8] != '':
        cursor.execute("""SELECT insert_edu(%s, %s, %s)""", (line[2], line[8], line[9]))
        connection.commit()
    else:
        print line[2]
        print line[9]
        print line[8]
        print 'error'''''

for line in csv.reader(input_file2, delimiter=str('|')):
    if count == 0:
        count += 1
        continue

    # try:
    if line[9] != '' or line[8] != '':
        cursor.execute("""SELECT insert_edu(%s, %s, %s)""", (line[2], line[4], line[7]))
        connection.commit()
    else:
        print line[2]
        print line[9]
        print line[8]
        print 'error'
    # except:
    # print 'Execute Failed'
    # logger.logger.info('Execute Failed.')
