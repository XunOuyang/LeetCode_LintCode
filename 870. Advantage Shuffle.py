# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 22:58:50 2018

@author: TZLMYQ
"""

class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        if not A or len(A) == 1:
            return A
        length = len(A)
        for i in range(len(B)):
            B[i] = [B[i], i]      
        A.sort()
        B.sort()
        count = 0
        index_a, index_b = 0, 0
        while index_a < len(A):
            while index_a < len(A) and A[index_a] <= B[index_b][0]:
                index_a += 1
                count += 1
            else:
                index_a += 1
                index_b += 1
        res = [None]*length        
        for i in range(length - count):
            res[B[i][1]] = A[i+count]    
        for i in range(length - count, length):
            res[B[i][1]] = A[i+count-length]
        return res

solution = Solution()
A =  [2,0,4,1,2]
B = [1,3,0,0,2]

print solution.advantageCount(A, B)