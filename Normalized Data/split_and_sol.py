# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 13:57:53 2020

@author: Yong Sheng
"""

import subprocess
from apriorisplit import convertionista
import shutil
import os

def file_read(path):
    r = open(path)
    x = r.readlines()
    r.close()
    return x

############### FOR INITIAL GIVEN INSTANCES #####################

# #This part converts all .txt files, which have been converted to TSPLIB format, and to create both split formats out of it.
path = '.\\SDVRP instances'
dirs = tuple(os.walk(path))
for i in dirs[1:]:
    for j in i[2]:
        if j[-3:] == 'txt':
            p = i[0]+'\\'+j
            convertionista(p)

# #This part takes in all the .vrp files, and the .txt files, and runs them through vrp_rtr.exe.
path = '.\\SDVRP instances'
dirs = tuple(os.walk(path))
for i in dirs[1:]:
    shutil.copy(path+'\\vrp_rtr.exe', i[0])
    os.chdir(i[0])
    for j in i[2]:
        if j[-3:] == 'vrp' or j[-3:] == 'txt':
            subprocess.Popen('powershell.exe .\\vrp_rtr.exe -f ' + j + ' -out '+ j[:-4] + '.sol')


############### FOR CUSTOM INSTANCES #####################

# #This part converts all .txt files, which have been converted to TSPLIB format, and to create both split formats out of it.
path = '.\\'
dirs = tuple(os.walk(path))
for i in dirs[0][2]:
    if i[-3:] == 'txt':
        p = i
        convertionista(path + '\\' + p)

# #This part takes in all the .vrp files, and the .txt files, and runs them through vrp_rtr.exe.
path = '.\\'
entries = os.listdir('.\\')
os.chdir(path)
for i in entries:
    if i[-3:] == 'txt' or i[-3:] == 'vrp':
        subprocess.call('powershell.exe .\\vrp_rtr.exe -f ' + i + ' -out '+ i[:-4] + '.sol')
