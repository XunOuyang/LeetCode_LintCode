# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 16:41:07 2018

@author: tzlmyq
"""

class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [i for i in range(n+1)]
        for i in range(1, n):
            j = 2
            while i*j <= n:
                dp[i*j] = min(dp[i*j], dp[i]+j)
                j += 1
        print dp
        return dp[-1]
    
    
solution = Solution()
n = 18
print solution.minSteps(n)