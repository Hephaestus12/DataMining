#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 23:52:46 2020

@author: tejsukhatme
"""

with open('../data/MergedWithHealthLevels.csv', 'r') as data:
    dataList = list(data)
    headingRow = True
    
    num_back_conc = 0
    num_general_conc = 0
    num_lower = [0 for i in range(5)]
    num_higher = [0 for i in range(5)]
    num_back_conc_lower = [0 for i in range(5)]
    num_back_conc_higher = [0 for i in range(5)]
    
    #print (num_lower)
    
    for row in dataList:
        if headingRow:
            headingRow = False
            continue
        rowList = row.split(",")
        #print(rowList[22])
    
        num_back_conc += int(rowList[16])
        num_lower[int(rowList[22])] += 1
        num_higher[int(rowList[23])] += 1
        
        #print(rowList[20])
        if (int(rowList[16]) == 1):
            num_back_conc_lower[int(rowList[22])] += 1
            num_back_conc_higher[int(rowList[23])] += 1
    
    num_gen_conc = 495-num_back_conc
    
    print (num_lower)
    print (num_higher)
    print (num_back_conc_lower)
    print (num_back_conc_higher)
    print (num_back_conc)

    
    for i in range(5) :
        if i != 0 :
            print('Considering rule : [ Backward classes --> lower level '+str(i)+' treatment ]')
            print('\tSupport = ' + str(num_back_conc/495))
            print('\tConfidence = '+str(num_back_conc_lower[i]/num_back_conc))
            if num_lower[i]>0:
                print('\tLift = '+str(num_back_conc_lower[i]*495/(num_back_conc*num_lower[i])))
            print()
    print()
    print()
    
    for i in range(5) :
        if i != 0 :
            print('Considering rule : [ Backward classes --> higher level '+str(i)+' treatment ]')
            print('\tSupport = ' + str(num_back_conc/495))
            print('\tConfidence = '+str(num_back_conc_higher[i]/num_back_conc))
            if num_higher[i] > 0 :
                print('\tLift = '+str(num_back_conc_higher[i]*495/(num_back_conc*num_higher[i])))
            print()
 