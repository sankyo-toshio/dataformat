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
        # aaa = ['alexaSaystime','alexaIntenttime', 'botSaystime', 'Z\'', 'testreplytime', ' ', '}', ',']
        aaa = ['beforecontinueConversationtimne ','beforesendMessage ', 'timestamp: \'2018-09-18T', 'Z\'', 'beforeEnque response from bot ', ' ', '}', ',']
        for a in aaa:
            if line.find(a) != -1:
                line = re.sub(a, '', line)
        line = re.sub('\\.', ':', line)

        try:
            d = line.replace('\r','')
            d = d.replace('\n','')
            d = d.split('\t')  # ['04:19:11:136', '04:20:06:679', '04:20:37:817',...
            print(d)
            counter = 0
            for f in d:
                counter += 1
                if len(f) >= 15:
                    f = f[0:14]
                dt = datetime.strptime(f, '%H:%M:%S:%f')
                print(dt.hour)
                if counter == 1:
                    line = ""

                if counter == len(d):
                    line += str(dt.second) + '.' + str(dt.microsecond) + '\n'
                else:
                    line += str(dt.second) + '.' + str(dt.microsecond) + '\t'
        except:
            pass

        write_file.write(line)
finally:
    read_file.close()
    write_file.close()

# if os.path.isfile(sys.argv[1]) and os.path.isfile(temp_file):
#     os.remove(sys.argv[1])
#     os.rename(temp_file, sys.argv[1])
sys.exit(0)