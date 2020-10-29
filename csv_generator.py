# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:41:57 2020

@author: Yong Sheng
"""
import os
import numpy as np
def distance(x, y):
    return (x**2 + y**2)**(1/2)
def file_read(path):
    r = open(path)
    x = r.readlines()
    r.close()
    return x
path = '.\\SDVRP instances'
dirs = tuple(os.walk(path))
final_dict = {
    'initial_name': [],	
    'capacity': [],
    'number_of_nodes': [],	
    'highest_dist': [],	
    'lowest_dist': [],	
    'mean_dist': [],	
    'median_dist': [],	
    '25th_dist': [],	
    '75th_dist': [],	
    'sd_dist': [],	
    'highest_demand': [],	
    'lowest_demand': [],	
    'mean_demand': [],	
    'median_demand': [],	
    '25th_demand': [],	
    '75th_demand': [],
    'sd_demand': [],	
    'split_in_10x': [],	
    'split_in_rounded': []}
for i in dirs[1:]:
    for j in i[2]:
        if j[-3:] == 'txt':
            distances = []
            demands = []
            x = file_read(i[0]+'\\'+j)
            name, cap = x[0].split('\\')[-1].split()[-1], x[4].split()[1]
            first_cut_idx = x.index("NODE_COORD_SECTION\n")
            second_cut_idx = x.index('DEMAND_SECTION\n')
            third_cut_idx = x.index('DEPOT_SECTION\n')
            x2 = x[first_cut_idx+1:second_cut_idx]
            x3 = x[second_cut_idx+1:third_cut_idx]
            for index in range(1, len(x2)):
                _, a, b = x2[index].split()
                _, c = x3[index].split()
                a, b, c = int(a), int(b), int(c)
                dist = distance(a, b)
                distances.append(dist)
                demands.append(c)
            final_dict['initial_name'].append(name)
            final_dict['capacity'].append(cap)
            final_dict['number_of_nodes'].append(len(x2) - 1)
            final_dict['highest_dist'].append(max(distances))
            final_dict['lowest_dist'].append(min(distances))
            final_dict['mean_dist'].append(np.mean(distances))
            final_dict['median_dist'].append(np.median(distances))
            final_dict['25th_dist'].append(np.percentile(distances, 25))
            final_dict['75th_dist'].append(np.percentile(distances, 75))
            final_dict['sd_dist'].append(np.std(distances))
            final_dict['highest_demand'].append(max(demands))
            final_dict['lowest_demand'].append(min(demands))
            final_dict['mean_demand'].append(np.mean(demands))
            final_dict['median_demand'].append(np.median(demands))
            final_dict['25th_demand'].append(np.percentile(demands, 25))
            final_dict['75th_demand'].append(np.percentile(demands, 75))
            final_dict['sd_demand'].append(np.std(demands))





'''
initial_name	
capacity	
number_of_nodes	
highest_dist	
lowest_dist	
mean_dist	
median_dist	
25th_dist	
75th_dist	
sd_dist	
highest_demand	
lowest_demand	
mean_demand	
median_demand	
25th_demand	
75th_demand	
sd_demand	
split_in_10x	
split_in_rounded
'''