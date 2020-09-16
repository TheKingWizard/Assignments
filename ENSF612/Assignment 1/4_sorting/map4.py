#!/usr/bin/env python
#map4.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
        if word is '':
            continue
        print(word[:1] + '\t' + word)
