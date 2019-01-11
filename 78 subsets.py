# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 10:01:41 2019

@author: TZLMYQ
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path[:])
        for i in xrange(index,len(nums)):
            path.extend([nums[i]])
            self.dfs(nums, i+1, path, res)
            path.pop()
            
            
    """
    The code above is more standardized. Save as C++
    the code above equals to the code below:
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index,len(nums)):
            self.dfs(nums, i+1, path + [nums[i]], res)
    
    """