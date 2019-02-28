# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 15:55:15 2018

@author: TZLMYQ
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        if nums == []:
            return []
        elif len(nums) == 1:
            return [nums]
        i = 0
        while i < len(nums):
            if i + 1 < len(nums):
                if nums[i] != nums[i + 1]:
                    m = nums[i]
                    leftNums = nums[:i] + nums[i + 1:]
                    for item in self.permuteUnique(leftNums):
                        res.append([m] + item)
                i += 1
            else:
                m = nums[i]
                leftNums = nums[:i] + nums[i + 1:]
                for item in self.permuteUnique(leftNums):
                    res.append([m] + item)
                i += 1
        return res
                
