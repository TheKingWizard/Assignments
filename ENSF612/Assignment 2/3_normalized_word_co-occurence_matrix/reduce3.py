#!/usr/bin/env python
#reduce3.py

import string
import sys

current_item1 = None
current_item2 = None
num = 1
total_num = 1

for line in sys.stdin:
    line = line.strip()
    item1, item2 = line.split(' ')

    if current_item1 is None:
        current_item1 = item1
        continue

    if item1 == current_item1:
        if item2 == '*':
            total_num += 1
            continue
        elif current_item2 is None :
            current_item2 = item2
            continue

        if item2 == current_item2:
            num += 1
        else:
            print('%s %s %s' % (current_item1, current_item2, str(num / float(total_num))))
            num = 1
            current_item2 = item2

    else:
        current_item1 = item1
        current_item2 = None
        total_num = 1

print('%s %s %s' % (current_item1, current_item2, str(num / float(total_num))))
