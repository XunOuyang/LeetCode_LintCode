# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 18:33:55 2018

@author: tzlmyq
"""
import collections
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if not start or not end or len(start) != len(end):
            return False
        if collections.Counter(start) != collections.Counter(end):
            return False
        L, R = 0, 0
        for i in range(len(start)):
            if start[i] == "R":
                R += 1
            if start[i] == "L":
                L += 1
            if end[i] == "R":
                if L > 0:
                    return False
                else:
                    R -= 1
            if end[i] == "L":
                if R > 0:
                    return False
                else:
                    L -= 1          
        return L == 0 and R == 0
    
    
solution = Solution()
start = "XXXXXLXXXX"
end =   "XXXXXXXLXX"
print solution.canTransform(start, end)