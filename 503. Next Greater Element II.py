# -*- coding: utf-8 -*-
"""
这道题最tricky的地方在于，我们需要用stack记住的是每个数字的index，而不是数字本身。
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        nums = nums + nums
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            if i < len(nums)/2:
                stack.append(i)
        return res
                    
    
solution = Solution()
nums = [2,1,2]
print solution.nextGreaterElements(nums)
