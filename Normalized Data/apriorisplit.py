# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os

def file_read(path):
    r = open(path)
    x = r.readlines()
    r.close()
    return x

def splitter(location, demand, capacity):
    cap_splits = [int(int(capacity) * 0.2), int(int(capacity) * 0.1), int(int(capacity) * 0.05), int(round(int(capacity) * 0.01))]
    print(cap_splits)
    number_of_nodes = len(demand)
    inc = 2
    final = ['1 0']
    final_loc = ['1 0.00000 0.00000']
    for i in range(1, number_of_nodes):
        t = int(demand[i].split()[1])
        loc = location[i].split(' ', 1)[1]
        while t >= cap_splits[0]:
            final.append(str(inc) + ' ' + str(cap_splits[0]))
            final_loc.append(str(inc) + ' ' + loc.strip())
            t -= cap_splits[0]
            inc += 1
        while t >= cap_splits[1]:
            final.append(str(inc) + ' ' + str(cap_splits[1]))
            final_loc.append(str(inc) + ' ' + loc.strip())
            t -= cap_splits[1]
            inc += 1
        while t >= cap_splits[2]:
            final.append(str(inc) + ' ' + str(cap_splits[2]))
            final_loc.append(str(inc) + ' ' + loc.strip())
            t -= cap_splits[2]
            inc += 1
        while t >= cap_splits[3]:
            final.append(str(inc) + ' ' + str(cap_splits[3]))
            final_loc.append(str(inc) + ' ' + loc.strip())
            t -= cap_splits[3]
            inc += 1
        if t > 0:
            final.append(str(inc) + ' ' + str(int(round(t))))
            final_loc.append(str(inc) + ' ' + loc.strip())
            t -= cap_splits[3]
            inc += 1
    return '\n'.join(final_loc), '\n'.join(final), inc

def convertionista(path):
    x = file_read(path)
    print(path)
    # Finding the correct indexes and splitting the list into two lists: one with the location of each node and one with the demand of each node
    name, cap = x[0].split()[1], x[4].split()[1]
    first_cut_idx = x.index("NODE_COORD_SECTION\n")
    second_cut_idx = x.index('DEMAND_SECTION\n')
    third_cut_idx = x.index('DEPOT_SECTION\n')
    x2 = x[first_cut_idx+1:second_cut_idx]
    x3 = x[second_cut_idx+1: third_cut_idx]
    x3_times_10 = []
    for i in x3:
        spt = i.split()
        spt[1] = str(int(spt[1])*10)
        spt = ' '.join(spt)
        x3_times_10.append(spt)
    new_locs, new_dems, num_elems = splitter(x2, x3, cap)
    index_check = 0
    while os.path.isfile(name + "_split" + str(index_check) + ".vrp"):
        index_check += 1
    f = open(path[:-4] + "_split" + str(index_check) + ".vrp", "x")
    f.write('NAME:' + name + '_split\nBEST_KNOWN: 0\nCOMMENT: 0\nDIMENSION: ' + str(num_elems-1) + '\nCAPACITY: ' + str(int(cap)) + '\nEDGE_WEIGHT_FORMAT: FUNCTION\nEDGE_WEIGHT_TYPE: EXACT_2D\nNODE_COORD_SECTION\n')
    f.write(new_locs)
    f.write('\nDEMAND_SECTION\n')
    f.write(new_dems)
    f.write('\nDEPOT_SECTION\n1\n-1\nEOF')
    f.close()
    
    new_locs, new_dems, num_elems = splitter(x2, x3_times_10, int(cap)*10)
    index_check = 0
    while os.path.isfile(name + "_splitx10_" + str(index_check) + ".vrp"):
        index_check += 1
    f = open(path[:-4] + "_splitx10_" + str(index_check) + ".vrp", "x")
    f.write('NAME:' + name + '_splitx10_\nBEST_KNOWN: 0\nCOMMENT: 0\nDIMENSION: ' + str(num_elems-1) + '\nCAPACITY: ' + str(int(cap)*10) + '\nEDGE_WEIGHT_FORMAT: FUNCTION\nEDGE_WEIGHT_TYPE: EXACT_2D\nNODE_COORD_SECTION\n')
    f.write(new_locs)
    f.write('\nDEMAND_SECTION\n')
    f.write(new_dems)
    f.write('\nDEPOT_SECTION\n1\n-1\nEOF')
    f.close()

'''
NAME: Christofides-1
BEST_KNOWN: 524.61
COMMENT: 524.610000
DIMENSION: 5
CAPACITY: 160
EDGE_WEIGHT_FORMAT: FUNCTION
EDGE_WEIGHT_TYPE: EXACT_2D
NODE_COORD_SECTION
1 0.00000 0.00000
2 7.00000 12.00000
3 19.00000 9.00000
4 19.00000 9.00000
5 22.00000 24.00000
DEMAND_SECTION
1 0
2 7
3 30
4 16
DEPOT_SECTION
1
-1
EOF
'''
