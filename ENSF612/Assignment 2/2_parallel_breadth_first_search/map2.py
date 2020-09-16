#!/usr/bin/env python
#map2.py

import string
import sys


for line in sys.stdin:
    line = line.strip()
    node,val = line.split('\t')
    values = val.split('|')
    adjacency_list = values[0].split(',')
    distance = values[1]
    if distance != 'Integer.MAX_VALUE':
        distance = int(distance)
    color = values[2]
    parent = values[3]
    if color == 'GRAY':
        for n in adjacency_list:
            print('%s\t%s|%s|%s|%s' %(n,'null',str(distance + 1),'GRAY',node))
        print('%s\t%s|%s|%s|%s' %(node,','.join(adjacency_list),str(distance),'BLACK',parent))
    if color == 'WHITE' or color == 'BLACK':
        print('%s\t%s|%s|%s|%s' %(node,','.join(adjacency_list),str(distance),color,parent))
