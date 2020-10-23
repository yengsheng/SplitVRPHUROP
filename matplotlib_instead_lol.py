# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 19:59:37 2020

@author: Yong Sheng
"""
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import os

def file_read(path):
    r = open(path)
    x = r.readlines()
    r.close()
    return x

info_dump = {}
count = 0
path = 'C:\\Users\\Yong Sheng\\Desktop\\UROP\\SplitVRPHUROP\\SDVRP instances'
dirs = tuple(os.walk(path))
col_num = 0
for directory in dirs[1:]:
    for file_name in directory[2]:
        print(file_name)
        verts = []
        codes = []
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
        
        fig, ax = plt.subplots()
        visited = []
        for i in route_list:
            verts.append((0,0))
            codes.append(Path.MOVETO)
            for j in i:
                goto_traj = (node_dict[abs(int(j))+1][0], node_dict[abs(int(j))+1][1])
                verts.append(goto_traj)
                codes.append(Path.MOVETO)
                if goto_traj in visited and goto_traj != visited[-1]:
                    info_dump[file_name].append(goto_traj)
                visited.append(goto_traj)
            verts.append((0,0))
            codes.append(Path.MOVETO)
        xs, ys = zip(*verts)
        ax.plot(xs, ys, 'x--', lw=1, color='black', ms=3)
        
        ax.set_xlim(-50, 50)
        ax.set_ylim(-50, 50)
        plt.show()
        plt.savefig(directory[0]+'\\'+file_name[:-4]+'.png', dpi=120)
        plt.close()