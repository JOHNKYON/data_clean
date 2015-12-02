# -*- coding: utf-8 -*-

import csv
import codecs
import pandas

reader = csv.reader(codecs.open('./utf8/Cveducation_cn_1.txt', 'rb'))
for line in reader:
    print line[2]

'''reader = pandas.read_csv('./utf8/Cveducation_cn_1.txt', encoding='utf-8')
print reader[:3]'''
