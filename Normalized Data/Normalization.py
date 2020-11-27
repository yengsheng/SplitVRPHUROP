# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:54:04 2020

@author: Yong Sheng
"""

import subprocess
# from apriorisplit import convertionista
import shutil
import os

def file_read(path):
    r = open(path)
    x = r.readlines()
    r.close()
    return x

def normalize(file):
    x = file_read(file)
    name = file[:-4]
    cap = x[4].split()[1]
    print(name, cap)
    div = int(cap)/100
    second_cut_idx = x.index('DEMAND_SECTION\n')
    third_cut_idx = x.index('DEPOT_SECTION\n')
    x3 = x[second_cut_idx+1: third_cut_idx]
    new_demands = []
    for j in x3:
        d = j.split()[1].strip()
        new_demands.append(j.split()[0] + ' ' + str(int(int(d)/div)) + '\n')
    new_txt = 'NAME: '  + name + '_NORMALIZED\n' + ''.join(x[1:4]) + 'CAPACITY: 100\n' + ''.join(x[5:second_cut_idx+1]) + ''.join(new_demands) + 'DEPOT_SECTION\n1\n-1\nEOF'  
    f = open(name+'_normalized.txt', "x")
    f.write(new_txt)
    f.close()
    
path = '.\\'
dirs = tuple(os.walk(path))

for i in dirs[0][2]:
    if i[-3:] == 'txt':
        normalize(i)
        
