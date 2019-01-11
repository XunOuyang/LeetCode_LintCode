# -*- coding: utf-8 -*-
"""
Created on Sun Oct 07 22:58:54 2018

@author: TZLMYQ
"""

class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type A: List[int]
        :rtype: int
        """
        local_min, local_max, res_loc, res_max = nums[0], nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            local_max = max(local_max + nums[i], nums[i])
            local_min = min(local_min + nums[i], nums[i])
            res_loc = min(res_loc, local_min)
            res_max = max(local_max, res_max)
        if sum(nums) != res_loc:
            res = max(sum(nums)-res_loc, res_max)
        else:
            res = res_max
        return res
    
solution = Solution()
nums = [-2, -3, -1]
print(solution.maxSubarraySumCircular(nums))