#!/usr/bin/env python
#map1.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    row,col,val = line.split(',')
    print('%s,%s,%s' %(col,row,val))
    