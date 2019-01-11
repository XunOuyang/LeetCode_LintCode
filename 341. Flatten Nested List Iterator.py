# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 23:51:21 2018

@author: TZLMYQ
"""

"""
this is a flatten nested list iterator follow up question

"""

def nestedInteger( nestedList):
    res = []
    def unpack(nestedList):
        for top in nestedList:
            if type(top) != type(res):
                res.append(top)
            else:
                unpack(top)
    unpack(nestedList)
    return res
    
                
#solution = Solution()
nestedList = [[1,1],2,[1,1]]
print nestedInteger(nestedList)