# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 10:04:20 2018

@author: TZLMYQ
"""

"""
the key to solve this problem is to find the formula that n = (n - 1)/26
it`s easy to make a mistake like n = n /27 - 1
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n > 0:
            res += chr((n- 1) % 26 + ord("A") )
            n = (n - 1)/26
        return res[::-1]
    
    
solution = Solution()
n = 26
print solution.convertToTitle(n)