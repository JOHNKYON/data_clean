# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import unicode_literals

import csv
import codecs
import heapq


# 打开文件
input_file1 = codecs.open('./utf8/Cveducation_cn_1.txt', 'rb')
input_file2 = codecs.open('./utf8/Cvworkexp_cn_1.txt', 'rb',)
output_file = codecs.open('./utf8/identify.txt', 'w', encoding='utf-8')

heap1 = []
heap2 = []
count = 0

# file1 = input_file1.readlines()
for line in csv.reader(input_file1):
    try:
        temp = long(line[2])
    except:
        # print "fisrt line"
        continue
    try:
        # heap1.append(temp)
        heapq.heappush(heap1, temp)
    except:
        print "literate invalid"
    '''except:
        print "literate invalid"
        print line_list[2]
        raw_input()'''
input_file1.close()

print "file1 finished"
raw_input()

for line in csv.reader(input_file2):
    try:
        temp = long(line[2])
    except:
        continue
    try:
        # heap2.append(temp)
        heapq.heappush(heap2, temp)
    except:
        print "literate invalid"
input_file2.close()

print "file2 finished"

while len(heap1) != 0 and len(heap2) != 0:
    count += 1
    print count
    temp = '1: ' + str(heapq.heappop(heap1)) + '\t' + '2:' + str(heapq.heappop(heap2)) + '\n'
    output_file.write(temp)

if len(heap1) != 0:
    count += 1
    print count
    while len(heap1) != 0:
        temp = '1: ' + str(heapq.heappop(heap1)) + '\t' + '2:' + '0' + '\n'
        output_file.write(temp)

if len(heap2) != 0:
    count += 1
    print count
    while len(heap2) != 0:
        temp = '1: ' + '0' + '\t' + '2:' + str(heapq.heappop(heap2)) + '\n'
        output_file.write(temp)

output_file.close()
