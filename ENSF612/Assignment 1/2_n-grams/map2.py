#!/usr/bin/env python
#map2.py

import string
import sys

w1 = None
w2 = None

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
        if word is "":
            continue
        if w1 is None:
            w1 = word
            continue
        elif w2 is None:
            w2 = word
        else:
            w1 = w2
            w2 = word
        print('%s %s\t%s' %(w1,w2,1))
