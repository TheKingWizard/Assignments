#!/usr/bin/env python
#reduce2.py

import string
import sys

current_node = None
current_adjacency_list = None
current_distance = None
current_color = None
current_parent = None

for line in sys.stdin:
    line = line.strip()
    node,val = line.split('\t')
    values = val.split('|')
    adjacency_list = values[0]
    if adjacency_list == 'null':
        adjacency_list = None
    else:
        adjacency_list = adjacency_list.split(',')
    distance = values[1]
    if distance == 'Integer.MAX_VALUE':
        distance = -1
    else:
        distance = int(distance)
    color = values[2]
    parent = values[3]

    if parent == 'null':
        parent = None

    if current_node is None:
        current_node = node
        current_adjacency_list = adjacency_list
        current_distance = distance
        current_color = color
        current_parent = parent
    elif node == current_node:
        if adjacency_list is not None:
            current_adjacency_list = adjacency_list
        if (current_distance == -1) or (distance != -1 and distance < current_distance):
            current_distance = distance
            current_parent = parent
        if (current_color == 'WHITE' and color == 'GRAY') or (current_color == 'GRAY' and color == 'BLACK'):
            current_color = color
        
    elif node != current_node:
        if current_distance == -1:
            current_distance = 'Integer.MAX_VALUE'
        print('%s\t%s|%s|%s|%s' %(current_node,
                                ','.join(current_adjacency_list),
                                str(current_distance),
                                current_color,
                                current_parent))
        if current_color != 'BLACK':
            sys.stderr.write("reporter:counter:GRAPH,NON_BLACK,1\n")
        current_node = node
        current_adjacency_list = adjacency_list
        current_distance = distance
        current_color = color
        current_parent = parent

if current_distance == -1:
    current_distance = 'Integer.MAX_VALUE'
if current_color != 'BLACK':
            sys.stderr.write("reporter:counter:GRAPH,NON_BLACK,1\n")
print('%s\t%s|%s|%s|%s' %(current_node,
                        ','.join(current_adjacency_list),
                        str(current_distance),
                        current_color,
                        current_parent))
