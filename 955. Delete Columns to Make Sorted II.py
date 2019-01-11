# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 23:07:07 2018

@author: TZLMYQ
"""

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = 0
        if not A:
            return res
        for i in range(len(A[0])):
            j = 0
            flag = False
            while j < len(A)-1:
                if A[j][i] < A[j+1][i]:
                    j += 1
                elif A[j][i] == A[j+1][i]:
                    j += 1
                    flag = True
                else:
                    res += 1
                    print(res, i, j)
                    break
                
            if res == i and flag == False:
                return res
        return res

solution = Solution()
A = ["abx","agz","bgc","bfc"]
print(solution.minDeletionSize(A))