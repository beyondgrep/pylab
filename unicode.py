#!/usr/bin/env python

import re

filepath = 'README_win32.pod'
regex = re.compile('fa')
with open(filepath, 'r', encoding='ISO8859') as fh:
    n = 0
    line = fh.readline()
    while line:
        print(line)
        n += 1
        line = line.rstrip()
        match = re.search(regex, line)
        if match:
            print(line)
        line = fh.readline()
    fh.close()
