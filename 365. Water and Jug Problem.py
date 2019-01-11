# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 22:24:03 2018

@author: tzlmyq
"""

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x == z or y == z:
            return True
        elif x == 0 and y == 0:
            return z == 0
        elif x + y < z:
            return False
        if x < y:
            x, y = y, x
        while y != 0 and x != y:
            remainder = x % y
            x = y
            y = remainder
        
        if y == 0:
            return z % x == 0
        else:
            return z % y == 0
        
    
solution = Solution()
x = 3
y = 6
z = 5
print(solution.canMeasureWater(x, y, z))