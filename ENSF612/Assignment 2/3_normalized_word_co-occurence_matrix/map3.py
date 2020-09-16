#!/usr/bin/env python
#map3.py

import string
import sys

for line in sys.stdin:
    line = line.strip()
    items = line.split(' ')
    for item in items:
        for item2 in items:
            if item2 is not item:
                print('%s %s' % (item, item2))
                print('%s *' % item)
