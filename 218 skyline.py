# -*- coding: utf-8 -*-
"""
Created on Sun May 13 23:35:40 2018

@author: tzlmyq
"""

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        
        
        ''' this method works but MLE
        buildings = sorted(buildings, key = lambda building:building[1])
        rebuilt = [0] * (buildings[-1][1] + 1)
        for building in buildings:
            for i in range(building[0], building[1]):
                rebuilt[i] = max(building[2], rebuilt[i])
        res = []
        rebuilt.insert(0, 0)
        for i in range(1, len(rebuilt)):
            if rebuilt[i] != rebuilt[i-1]:
                res.append([i -1, rebuilt[i]])
        return res
        '''
        
solution = Solution()

buildings = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ]

print solution.getSkyline(buildings)