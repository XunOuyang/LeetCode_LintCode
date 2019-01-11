# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:16:54 2018

@author: TZLMYQ
"""

class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        # this is a binary search problem
        if K > N:
            return -1
        count = 0
        left, right = 1, N
        target1, target2 = 0, N+1
        while target1 != target2-1:
            mid = (left+right)/2
            if mid >= K:
                right = mid
                target2 = right+1
            else:
                left = mid+1
                target1 = left
            count += 1
            print mid
        return count
    
    
solution = Solution()
K = 1
N = 2 
print(solution.superEggDrop(K, N))