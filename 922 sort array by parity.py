# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 22:16:14 2018

@author: tzlmyq
"""

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        left, right = 0, 0
        while right < len(A) and left < len(A):
            while A[left]%2 == left%2:
                left += 1
                if left == len(A):
                    return A
            right = left + 1
            while A[right]%2 == right%2:
                right += 1
            A[left], A[right] = A[right], A[left]
            if right == len(A):
                break
        return A
        
    
solution = Solution()
A = [4, 2, 5, 7]
print(solution.sortArrayByParityII(A))