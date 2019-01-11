# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:23:41 2018

@author: TZLMYQ
"""

class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if not A:
            return -1
        if max(A) >= K:
            return 1
        res = -1
        left, right = 0, 1
        s = A[0]
        while right < len(A):
            if s < 0:
                s = A[right]
            elif 
            
            
            while s < K:
                s += A[right]
                right += 1
                if s <= 0:
                    left = right
                    right += 1
                    s = A[right]
                elif right < len(A):
                    right += 1
                    s += A[right]
                else:
                    left += 1
                    s -= A[left-1]
            if res != -1:
                res = min(res, right - left + 1)
        return res
            
    
solution = Solution()
A = [2, -1, 2] 
K = 3
print(solution.shortestSubarray(A, K))
            
                