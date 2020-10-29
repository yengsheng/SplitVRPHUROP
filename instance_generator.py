# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 17:12:04 2020

@author: Yong Sheng
"""
import random

init_dic = {1: ['p01', 50, 160],
            2: ['p02', 75, 140],
            3: ['p03', 100, 200],
            4: ['p04', 150, 200],
            10: ['p10', 199, 200]}

def generate(num, startnum):
    all_text = "NAME: " + init_dic[num][0] + '_' + str(startnum) + '\nBESTKNOWN: 0\nCOMMENT: 0\nDIMENSION: ' + str(init_dic[num][1] + 1) + '\nCAPACITY: ' + str(init_dic[num][2]) + '\nEDGE_WEIGHT_FORMAT: FUNCTION\nEDGE_WEIGHT_TYPE: EXACT_2D\nNODE_COORD_SECTION\n1 0 0\n'
    for i in range(init_dic[num][1]):
        all_text = all_text + str(i+2) + ' ' + str(random.randint(-50, 50)) + ' ' + str(random.randint(-50, 50)) + '\n'
    all_text += 'DEMAND_SECTION\n1 0\n'
    for i in range(init_dic[num][1]):
        all_text += str(i+2) + ' ' + str(random.randint(int(init_dic[num][2]/8), int(init_dic[num][2]/2))) + '\n'
    all_text += 'DEPOT_SECTION\n1\n-1\nEOF'
    f = open(".\\SDVRP instances\\custom_instances\\" + init_dic[num][0] + '_' + str(startnum) + ".txt", "x")
    f.write(all_text)
    f.close()
    
for i in (1, 2, 3, 4, 10):
    for j in range(1, 31):
        generate(i, j)