# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:57:53 2020

@author: Yong Sheng
"""

import subprocess
from apriorisplit import convertionista
import shutil
import os
from turtle import *

# The following code makes the turtle move it move it.
turt_colors = ['red', 'blue', 'orange', 'green', 'purple', 'grey', 'black', 'brown', 'cyan', 'magenta', 'teal', 'olive', 'maroon']

def file_read(path):
    r = open(path)
    x = r.readlines()
    r.close()
    return x

# #This part converts all .txt files, which have been converted to TSPLIB format, and to create both split formats out of it.
# path = 'C:\\Users\\Yong Sheng\\Desktop\\UROP\\SplitVRPHUROP\\SDVRP instances'
# dirs = tuple(os.walk(path))
# for i in dirs[1:]:
#     for j in i[2]:
#         if j[-3:] == 'txt':
#             p = i[0]+'\\'+j
#             convertionista(p)

# #This part takes in all the .vrp files, and the .txt files, and runs them through vrp_rtr.exe.
# path = 'C:\\Users\\Yong Sheng\\Desktop\\UROP\\SplitVRPHUROP\\SDVRP instances'
# dirs = tuple(os.walk(path))
# for i in dirs[1:]:
#     shutil.copy(path+'\\vrp_rtr.exe', i[0])
#     os.chdir(i[0])
#     for j in i[2]:
#         if j[-3:] == 'vrp' or j[-3:] == 'txt':
#             subprocess.Popen('powershell.exe .\\vrp_rtr.exe -f ' + j + ' -out '+ j[:-4] + '.sol')

# This part saves the turtle plot into the respective folders.

info_dump = {}
bob = Turtle()
bob.speed(0)
setworldcoordinates(-50, -50, 50, 50)
path = 'C:\\Users\\Yong Sheng\\Desktop\\UROP\\SplitVRPHUROP\\SDVRP instances'
dirs = tuple(os.walk(path))
for directory in dirs[1:]:
    for file_name in directory[2]:
        if file_name[-3:] == 'sol' and os.path.isfile(directory[0]+'\\'+file_name[:-4]+'.vrp'):
            x, y = file_read(directory[0]+'\\'+file_name), file_read(directory[0]+'\\'+file_name[:-4]+'.vrp')
        elif file_name[-3:] == 'sol':
            x, y = file_read(directory[0]+'\\'+file_name), file_read(directory[0]+'\\'+file_name[:-4]+'.txt')
        else: continue
        paths = x[0].split()[1:]
        best = x[-3]
        info_dump[file_name] = [best]
        first_cut_idx = y.index("NODE_COORD_SECTION\n")
        second_cut_idx = y.index('DEMAND_SECTION\n')
        third_cut_idx = y.index('DEPOT_SECTION\n')
        
        locations = y[first_cut_idx+1:second_cut_idx]
        demands = y[second_cut_idx+1: third_cut_idx]
        node_dict = {}
        for i in range(len(locations)):
            n, x, y = locations[i].split()
            d = demands[i].split()[1]
            node_dict[int(n)] = [float(x), float(y), float(d)]
            
        negative_indexes = []
        for i in paths:
            if int(i) < 0:
                negative_indexes.append(paths.index(i)) 
        
        route_list = []
        for i in range(len(negative_indexes)-1):
            route_list.append(paths[negative_indexes[i] : negative_indexes[i+1]])

        col_num = 0
        visited = ['']
        for i in route_list:
            try:
                bob.pencolor(turt_colors[col_num])
            except IndexError:
                col_num = 0
            for j in i:
                goto_traj = [node_dict[abs(int(j))+1][0], node_dict[abs(int(j))+1][1]]
                bob.goto(goto_traj)
                bob.write(abs(int(j)))
                if goto_traj in visited and goto_traj != visited[-1]:
                    bob.stamp()
                    info_dump[file_name].append(goto_traj)
                visited.append(goto_traj)
                
            bob.goto(0, 0)
            col_num += 1
        
        ts = bob.getscreen()
        ts.getcanvas().postscript(file=directory[0]+'\\'+file_name[:-4]+'.eps')
        clearscreen()
        
            


