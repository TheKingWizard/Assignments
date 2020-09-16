#!/usr/bin/env python
#reduce3.py

import string
import sys

prev_key = None
tot_count = 0
filename = None
files = []
for line in sys.stdin:
    line = line.rstrip()
    word,file = line.split('\t')
    if prev_key==None:
        prev_key=word
        filename = file
        files.append(filename)
        continue
    if prev_key==word:
        if file != filename:
            filename = file
            files.append(filename)
        continue
    if prev_key!=word:
        print ('%s\t%s' %(prev_key,' '.join(files)))
        prev_key=word
        filename = file
        files = []
        files.append(filename)
print ('%s\t%s' %(prev_key,' '.join(files)))
