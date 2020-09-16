#!/usr/bin/env python
#reduce4.py

import string
import sys

prev_key = None
for line in sys.stdin:
#    print(line)
#    continue
    line = line.rstrip()
    c, word = line.split('\t')
#    word = line[3:]
    #print(c)
    #continue
    if prev_key==None:
        prev_key=word
        continue
    if prev_key==word:
        continue
    if prev_key!=word:
        print(prev_key)
	prev_key=word
print(prev_key)
    

