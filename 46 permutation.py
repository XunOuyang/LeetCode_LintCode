# -*- coding: utf-8 -*-
"""
Created on Mon Jul 09 22:20:53 2018

@author: TZLMYQ
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for i in range(len(nums)-1):            
            for j in range(i+1,len(nums)):
                temp = list(nums)
                temp[j],temp[i] = temp[i], temp[j]
                print temp
                res.append(temp)
                print res
                temp[j],temp[i] = temp[i], temp[j]
        return res
        
solution = Solution()
nums = [1,2,3]
print solution.permute(nums)
