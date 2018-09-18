#!/usr/bin/python
# coding: UTF-8

import re
import sys
import os
from datetime import datetime

read_file = None
write_file = None
temp_file = "bbb.txt"
try:
    read_file = open(sys.argv[1], 'r')
    write_file = open(temp_file, 'w')
    for line in read_file:
        aaa = ['alexaSaystime','alexaIntenttime', 'botSaystime', 'Z\'', 'testreplytime', ' ', '}', ',']
        for a in aaa:
            if line.find(a) != -1:
                line = re.sub(a, '', line)
        line = re.sub('\\.', ':', line)

        try:
            d = line.replace('\r','')
            d = d.replace('\n','')
            
            if len(d) >= 15:
                d = d[0:14]
            dt = datetime.strptime(d, '%H:%M:%S:%f')
            print(dt.hour)
            line = str(dt.second) + '.' + str(dt.microsecond) + '\n'
            # if line.find(sys.argv[2]) != -1:
            #     line = re.sub(sys.argv[2], sys.argv[3], line)
        except :
            pass

        write_file.write(line)
finally:
    read_file.close()
    write_file.close()

# if os.path.isfile(sys.argv[1]) and os.path.isfile(temp_file):
#     os.remove(sys.argv[1])
#     os.rename(temp_file, sys.argv[1])
sys.exit(0)