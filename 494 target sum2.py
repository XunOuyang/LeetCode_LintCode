# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 23:16:54 2018

@author: TZLMYQ
"""
import collections
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        d = collections.defaultdict()
        if nums[0] != 0:
            d[nums[0]] = 1
            d[-nums[0]] = 1
        else:
            d[0] = 2
        for i in range(1, len(nums)):
            num = nums[i]
            new_d = collections.defaultdict()
            for i in d:      
                new_d[i+num] = new_d.get(i+num, 0)+d.get(i, 0)
                new_d[i-num] = new_d.get(i-num, 0)+d.get(i, 0)
          #  d = self.union(d, new_d)
            d = new_d
        return d.get(S, 0)
    
    def union(self, dict1, dict2):
        return dict(list(dict1.items())+list(dict2.items()))
    
    
solution = Solution()
nums = [1, 1, 1, 1, 1]
S = 3
print(solution.findTargetSumWays(nums, S))