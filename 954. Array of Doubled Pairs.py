# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:16:19 2018

@author: TZLMYQ
"""

class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return True
        if len(A)%2==1:
            return False
        A.sort()
        left, right = 0, 1
        while left < len(A):
            print(A)
            if A[left] < 0:
                while right < len(A) and A[right]*2 < A[left]:
                    right += 1
                if right == len(A):
                    return False
                if A[right]*2 == A[left]:
                    A[right], A[left+1] = A[left+1], A[right]
                else:
                    return False
            
            elif A[left] == 0:
                if A[right] != 0:
                    return False
            else:
                while right < len(A) and A[right] < A[left]*2:
                    right += 1
                if right == len(A):
                    return False
                if A[right] == A[left]*2:
                    A[right], A[left+1] = A[left+1], A[right]
                else:
                    print(A)
                    return False      
            left += 2
            right = left + 1
        return True
                
solution = Solution()
A = [-1,4,6,8,-4,6,-6,3,-2,3,-3,-8]
print(solution.canReorderDoubled(A))