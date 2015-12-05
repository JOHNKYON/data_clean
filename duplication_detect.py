# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import codecs
import Levenshtein
import csv

input_file1 = codecs.open('./utf8/Cveducation_cn_1.txt', 'rb')
input_file2 = codecs.open('./utf8/Cvworkexp_cn_1.txt', 'rb',)
output_file1 = codecs.open('./utf8/edu_without_dup.txt', 'wb')
output_file2 = codecs.open('./utf8/work_without_dup.txt', 'wb')
writer1 = csv.writer(output_file1, delimiter=str('|'))
writer2 = csv.writer(output_file2, delimiter=str('|'))

temp = str()

# 判重并写入
for line in csv.reader(input_file1):
    if Levenshtein.distance(temp, line[9]) < 5:
        continue
    else:
        writer1.writerow(line)
        temp = line[9]

for line in csv.reader(input_file2):
    if Levenshtein.distance(temp, line[9]) < 5:
        continue
    else:
        writer2.writerow(line)
        temp = line[9]

input_file1.close()
input_file2.close()
output_file1.close()
output_file2.close()
