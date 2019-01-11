# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 10:01:03 2018

@author: tzlmyq
"""

class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 1
        if N % 2 == 1:
            res += 1
        for i in range(3, int(int((2*N-0.25)**0.5)+0.5)+1):
            if N % i == 0:
                res += 1
            
        return min(N, res)
    
    
solution = Solution()
N = 85
print(solution.consecutiveNumbersSum(N))