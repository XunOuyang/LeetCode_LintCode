# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 13:54:19 2018

@author: tzlmyq
"""

def missing4(arr):
    helper = [0 for i in range(4)]
    arr = arr + helper
    for i in range(len(arr)):
        if abs(arr[i]) <= len(arr) - 4:
            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1]
        else:
            arr[abs(arr[i]) - 1] = -1
    print arr
    res = []
    for i in range(len(arr)):
        if arr[i] >= 0:
            res.append(i + 1)
    print res
    return res
    
    
    """
    for i in range(len(arr)):
        temp = abs(arr[i])
        
        if(temp <= len(arr)):
            arr[temp-1] = arr[temp-1] * (-1)
            
        elif (temp > len(arr)):
            if (temp% len(arr)):
                helper[temp % len(arr) - 1] = -1
            else:
                helper[(temp % len(arr)) + len(arr) - 1] = -1
    
    for i in range(0, len(arr) ) :
        if (arr[i] > 0) :
            print((i + 1))
    for i in range(len(helper)):
        if(helper[i] >= 0):
            print((len(arr) + i + 1) )
    print arr, helper
    """
            
arr = [ 1, 7, 3, 12, 5, 10, 8, 4, 9 ]
missing4(arr)
 