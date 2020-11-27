# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 15:41:57 2020

@author: Yong Sheng
"""
import os
import numpy as np
import pandas as pd
def distance(x, y):
    return (x**2 + y**2)**(1/2)
def file_read(path):
    r = open(path)
    x = r.readlines()
    r.close()
    return x
path = '.\\'
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
    'original_objective': [],
    '10x_split_objective' : [],
    'rounded_split_objective': [],	
    'split_in_10x': [],	
    'split_in_rounded': [],
    'num_of_10x_splits': [],
    'num_of_rounded_splits': [],
    'highest_split_distance_10x': [],
    'highest_split_distance_rounded': []}

for i in dirs[0][2]:
    if i[-3:] == 'txt':
        
        final_dict['original_objective'].append(file_read(i[:-4] + '.sol')[7][:-2])
        distances = []
        demands = []
        x = file_read(i)
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
        x10file = file_read(i[:-4]  + '_splitx10_0.vrp')
        x10soln = file_read(i[:-4]  + '_splitx10_0.sol')
        rounddownfile = file_read(i[:-4]  + '_split0.vrp')
        rounddownsoln = file_read(i[:-4]  + '_split0.sol')
        paths = x10soln[0].split()[1:]
        first_cut_idx = x10file.index("NODE_COORD_SECTION\n")
        second_cut_idx = x10file.index('DEMAND_SECTION\n')
        third_cut_idx = x10file.index('DEPOT_SECTION\n')
        
        locations = x10file[first_cut_idx+1:second_cut_idx]
        demands = x10file[second_cut_idx+1: third_cut_idx]
        node_dict = {}
        for k in range(len(locations)):
            n, x, y = locations[k].split()
            d = demands[k].split()[1]
            node_dict[int(n)] = [float(x), float(y), float(d)]
            
        negative_indexes = []
        for l in paths:
            if int(l) < 0:
                negative_indexes.append(paths.index(l)) 
        
        route_list = []
        for m in range(len(negative_indexes)-1):
            route_list.append(paths[negative_indexes[m] : negative_indexes[m+1]])
        visited = ['']
        x10splits = []
        x10split_distances = []
        for locs in route_list:
            for loc in locs:
                goto_traj = [node_dict[abs(int(loc))+1][0], node_dict[abs(int(loc))+1][1]]
                if goto_traj in visited and goto_traj != visited[-1]:
                    x10splits.append([goto_traj])
                    x10split_distances.append((goto_traj[0]**2 + goto_traj[1]**2)**(1/2))
                visited.append(goto_traj)
        if x10splits == []:
            final_dict['num_of_10x_splits'].append(0)
            final_dict['split_in_10x'].append('no')
            final_dict['highest_split_distance_10x'].append(0)
        else:
            final_dict['num_of_10x_splits'].append(len(x10splits))
            final_dict['split_in_10x'].append('yes')
            final_dict['highest_split_distance_10x'].append(max(x10split_distances))
            
        final_dict['10x_split_objective'].append(x10soln[7][:-2])
        
        paths = rounddownsoln[0].split()[1:]
        first_cut_idx = rounddownfile.index("NODE_COORD_SECTION\n")
        second_cut_idx = rounddownfile.index('DEMAND_SECTION\n')
        third_cut_idx = rounddownfile.index('DEPOT_SECTION\n')
        
        locations = rounddownfile[first_cut_idx+1:second_cut_idx]
        demands = rounddownfile[second_cut_idx+1: third_cut_idx]
        node_dict = {}
        for k in range(len(locations)):
            n, x, y = locations[k].split()
            d = demands[k].split()[1]
            node_dict[int(n)] = [float(x), float(y), float(d)]
            
        negative_indexes = []
        for l in paths:
            if int(l) < 0:
                negative_indexes.append(paths.index(l)) 
        
        route_list = []
        for m in range(len(negative_indexes)-1):
            route_list.append(paths[negative_indexes[m] : negative_indexes[m+1]])
        visited = ['']
        rounddownsplits = []
        rounddown_distances = []
        for locs in route_list:
            for loc in locs:
                goto_traj = [node_dict[abs(int(loc))+1][0], node_dict[abs(int(loc))+1][1]]
                if goto_traj in visited and goto_traj != visited[-1]:
                    rounddownsplits.append([goto_traj])
                    rounddown_distances.append((goto_traj[0]**2 + goto_traj[1]**2)**(1/2))

                visited.append(goto_traj)
        if rounddownsplits == []:
            final_dict['num_of_rounded_splits'].append(0)
            final_dict['split_in_rounded'].append('no')
            final_dict['highest_split_distance_rounded'].append(0)

        else:
            final_dict['num_of_rounded_splits'].append(len(rounddownsplits))
            final_dict['split_in_rounded'].append('yes')
            final_dict['highest_split_distance_rounded'].append(max(rounddown_distances))

        final_dict['rounded_split_objective'].append(rounddownsoln[7][:-2])

df = pd.DataFrame(final_dict)
df.to_csv('dataset_2.csv', index=False)


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