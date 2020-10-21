# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:58:43 2020

@author: Yong Sheng
"""

from turtle import *

turt_colors = ['red', 'blue', 'orange', 'green', 'purple', 'grey', 'black', 'brown', 'cyan', 'magenta', 'teal', 'olive', 'maroon']

def file_read(path):
    r = open(path)
    x = r.readlines()
    r.close()
    return x

# x = file_read('x10_split_solution.txt')
# y = file_read('x10_split_instance.vrp')
def wild_turtle(sol, instance):
    x = file_read(sol)
    y = file_read(instance)
    
    # x = file_read('round_up_solution.txt')
    # y = file_read('round_up_instance.vrp')
    paths = x[0].split()[1:]
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
    
    bob = Turtle()
    bob.speed(0)
    setworldcoordinates(-50, -50, 50, 50)
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
                print(goto_traj)
            visited.append(goto_traj)
            
        bob.goto(0, 0)
        col_num += 1
    
    done()
    bye()  