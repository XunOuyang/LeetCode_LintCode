# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 13:00:45 2018

@author: tzlmyq
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # solution 1, it looks like a circle
        for i, num in enumerate(nums):
            print nums, i
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                temp = nums[i]                 
                nums[i] = nums[temp-1]
                nums[temp-1] = temp
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
        
        
        
    
solution = Solution()
nums = [3,4,-1,1]
print solution.firstMissingPositive(nums)