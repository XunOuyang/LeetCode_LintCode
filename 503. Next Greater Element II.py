# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 17:14:02 2018

@author: tzlmyq
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = []
        nums = nums + nums
        for i in range(len(nums)/2):
            j = 1
            while j < len(nums)/2:
                if nums[j+i] > nums[i]:
                    res.append(nums[j+i])
                    break
                j += 1
            if j == len(nums)/2:
                res.append(-1)
        return res
                    
    
solution = Solution()
nums = [2,1,2]
print solution.nextGreaterElements(nums)