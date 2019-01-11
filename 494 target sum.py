# -*- coding: utf-8 -*-
"""
Created on Mon Sep 03 16:03:42 2018

@author: TZLMYQ
"""

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums:
            return 0
        d = dict()
        d[nums[0]] = 1
        d[-nums[0]] = 1
        for i in range(1, len(nums)):
            new_d = dict()
            for i in d:      
                new_d[i+nums[i]] = new_d.get(i+nums[i], 0)+d.get(i, 0)
                new_d[i-nums[i]] = new_d.get(i-nums[i], 0)+d.get(i, 0)
            d = new_d
        return d.get(S, 0)
    
solution = Solution()
nums = [1, 1, 1, 1, 1]
S = 3
print solution.findTargetSumWays(nums, S)