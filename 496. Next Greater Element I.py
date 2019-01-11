# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 22:40:06 2018

@author: tzlmyq
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = dict()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    dic[nums[i]] = nums[j]
                    break
            if nums[i] not in dic:
                dic[nums[i]] = -1
        dic[nums[-1]] = -1
        res = []
        for i in range(len(findNums)):
            res.append(dic[findNums[i]])
        return res
    
solution = Solution()
findNums = [4,1,2]
nums =  [1,3,4,2]
print solution.nextGreaterElement(findNums, nums)

