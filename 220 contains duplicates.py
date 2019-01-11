# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 16:57:16 2018

@author: TZLMYQ
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0: 
            return False
        length = len(nums)
        for i in range(length):
            nums[i] = [nums[i], i]
        nums.sort()
        left, right = 0, 1
        while left < length:
            while right < length and nums[right][0] <= nums[left][0] +t:
                if abs(nums[right][1] -nums[left][1]) <= k and left < right :
                    print right, left, nums[right][0], nums[left][0]
                    return True
                else:
                    right += 1
            left += 1
        return False
                
            
            
            
solution = Solution()
nums = [1, 5, 9, 1, 5, 9]
k = 2
t = 3
print solution.containsNearbyAlmostDuplicate(nums, k, t)