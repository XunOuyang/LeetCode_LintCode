# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 20:27:42 2018

@author: TZLMYQ
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size
    
solution = Solution()
nums = [-10, -3, -2, -9] 
print solution.lengthOfLIS(nums)