# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def file_read(path):
    r = open(path)
    x = r.readlines()
    r.close()
    return x

def splitter(location, demand):
    number_of_nodes = len(demand)
    inc = 2
    final = ['1 0']
    final_loc = ['1 0.00000 0.00000']
    for i in range(1, number_of_nodes):
        t = int(demand[i].split()[1])
        loc = location[i].split(' ', 1)[1]
        while t >= 20:
            final.append(str(inc) + ' 20')
            final_loc.append(str(inc) + ' ' + loc.strip())
            t -= 20
            inc += 1
        while t >= 10:
            final.append(str(inc) + ' 10')
            final_loc.append(str(inc) + ' ' + loc.strip())
            t -= 10
            inc += 1
        while t >= 5:
            final.append(str(inc) + ' 5')
            final_loc.append(str(inc) + ' ' + loc.strip())
            t -= 5
            inc += 1
        while t >= 1:
            final.append(str(inc) + ' 1')
            final_loc.append(str(inc) + ' ' + loc.strip())
            t -= 1
            inc += 1
    return '\n'.join(final_loc), '\n'.join(final), inc

    
    
x = file_read('test_instance.txt')

# Finding the correct indexes and splitting the list into two lists: one with the location of each node and one with the demand of each node
name, cap = x[0].split()[1], x[4].split()[1]
first_cut_idx = x.index("NODE_COORD_SECTION\n")
second_cut_idx = x.index('DEMAND_SECTION\n')
third_cut_idx = x.index('DEPOT_SECTION\n')
x2 = x[first_cut_idx+1:second_cut_idx]
x3 = x[second_cut_idx+1: third_cut_idx]

new_locs, new_dems, num_elems = splitter(x2, x3)
f = open(name + "_split2.vrp", "x")
f.write('NAME:' + name + '_split\nBEST_KNOWN: 0\nCOMMENT: 0\nDIMENSION: ' + str(num_elems-1) + '\nCAPACITY: ' + str(cap) + '\nEDGE_WEIGHT_FORMAT: FUNCTION\nEDGE_WEIGHT_TYPE: EXACT_2D\nNODE_COORD_SECTION\n')
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
