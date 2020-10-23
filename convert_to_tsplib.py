# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 12:05:55 2020

@author: Yong Sheng
"""
import os

def convert(filename):
    f = open(filename)
    lines = f.readlines()
    nodes, capacity = lines[0].strip().split()
    nodes = int(nodes) + 1
    demands = ['0'] + lines[1].strip().split()
    locs = lines[2:]
    locs_stripped = []
    for i in locs:
        x = i.strip().split()
        temp = []
        for j in x:
            temp.append(int(j))
        locs_stripped.append(temp)
    init_x, init_y = locs_stripped[0]
    for i in locs_stripped[1:]:
        i[0] -= init_x
        i[1] -= init_y
    locs_stripped[0] = [0, 0]
    final = "NAME: " + filename[0:-4] + '\n' + 'BEST_KNOWN: 0\nCOMMENT: 0\nDIMENSION: ' + str(nodes) + '\nCAPACITY: ' + capacity + '\nEDGE_WEIGHT_FORMAT: FUNCTION\nEDGE_WEIGHT_TYPE: EXACT_2D\n'
    node_coord_section = 'NODE_COORD_SECTION\n'
    for i in range(1, nodes + 1):
        node_coord_section += str(i) + ' ' + str(locs_stripped[i-1][0]) + ' ' + str(locs_stripped[i-1][1]) + '\n'
    node_coord_section += 'DEMAND_SECTION\n'
    for i in range(1, nodes + 1):
        node_coord_section += str(i) + ' ' + demands[i-1] + '\n'
    node_coord_section += 'DEPOT_SECTION\n1\n-1\nEOF\n'
    
    index_check = 0
    while os.path.isfile(filename[0:-4] + "_tsplib" + str(index_check) + ".txt"):
        index_check += 1
    f = open(filename[0:-4] + "_tsplib" + str(index_check) + ".txt", "x")
    f.write(final)
    f.write(node_coord_section)
    f.close()
dirs = tuple(os.walk('.\\SDVRP instances'))
for i in dirs[1:]:
    for j in i[2]:
        if j[-4:] == '.cri':
            convert(i[0] + '\\' + j)


