# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 21:38:49 2018

@author: TZLMYQ
"""

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        n = bin(N)
        res = 0
        left = 0
        for i in range(2, len(n)):
            if n[i] == "1":
                if left == 0:
                    left = i
                else:
                    res = max(res, i - left)
                    left = i
        return res
    
    
solution = Solution()
N = 2
print solution.binaryGap(N)