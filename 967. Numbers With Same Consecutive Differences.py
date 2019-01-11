# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 22:17:15 2018

@author: TZLMYQ
"""

class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if K >= 10 or N == 0:
            return []
        if N == 1:
            return [i for i in range(10)]
        stack = [i for i in range(1, 10)]
        N -= 1
        while N:
            new_stack = []
            while stack:
                num = stack.pop()
                if num%10+K < 10:
                    new_stack.append(num*10+num%10+K)
                if num%10-K >=0:
                    new_stack.append(num*10+num%10-K)
            stack = new_stack
            N -= 1
        return list(set(stack))
        
solution = Solution()
N = 3
K = 2
print(solution.numsSameConsecDiff(N, K))