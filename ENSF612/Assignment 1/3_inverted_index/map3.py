#!/usr/bin/env python
#mapper.py

import string
import sys
import os

filename = os.environ["map_input_file"]
for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for word in words:
        for c in string.punctuation:
            word=word.replace(c,"")
        if word is "":
            continue
        print('%s\t%s' %(word,filename))
