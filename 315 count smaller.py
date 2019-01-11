# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 08:23:51 2018

@author: TZLMYQ
"""

"""


"""
import bisect

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        sorted_list = []
        for num in nums[::-1]:
            position = bisect.bisect_left(sorted_list, num)
            res.append(position)
            bisect.insort(sorted_list, num)
        return res[::-1]
    
    
solution = Solution()
nums = [5,2,6,1]
print solution.countLarger(nums)