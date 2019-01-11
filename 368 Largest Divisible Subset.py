# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 11:54:41 2018

@author: TZLMYQ
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = [1 for _ in range(len(nums))]
        for i in range(len(nums)):
            