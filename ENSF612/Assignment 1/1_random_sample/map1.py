#!/usr/bin/env python
#map.py

import string
import sys
import random

for line in sys.stdin:
    line = line.strip()
    if line is "":
        continue
    if random.randint(1,10) == 10:
        print(line)
