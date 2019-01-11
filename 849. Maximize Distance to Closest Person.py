# -*- coding: utf-8 -*-
"""
Created on Sat Jun 09 21:42:30 2018

@author: tzlmyq
"""

class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        if not seats or 0 not in seats:
            return 0
        if 1 not in seats:
            return len(seats)
        res = 0
        stack = []
        for i in range(len(seats)):
            if seats[i] == 1:
                if not stack:
                    res = max(i, res)
                    stack.append(i)
                else:
                    res = max((i - stack.pop())/2, res)
                    stack.append(i)
        if seats[-1] != 1:
            res = max(len(seats) - 1 - stack.pop(), res)
        return res
    
solution = Solution()
seats = [1,0,0,0,1]
print solution.maxDistToClosest(seats)