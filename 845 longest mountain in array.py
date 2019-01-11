# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:46:40 2018

@author: TZLMYQ
"""

class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A or len(A)<2:
            return 0
        flag = False
        length = 1
        res = 0
        for i in range(1, len(A)):
            # flag == True: mountain
            # flag == False: not a mountain
            if i >= 2 and A[i-2] < A[i-1] and A[i-1] > A[i]:
                flag = True
                length += 1
                res = max(res, length)
            elif A[i-1] > A[i] and flag == False:
                length = 1
            elif A[i-1] < A[i] and flag == False:
                length += 1
            elif A[i-1] < A[i] and flag == True:
                length = 2
                flag = False
            elif A[i-1] > A[i] and flag == True:                
                length += 1
                res = max(res, length)
        return res
    
    
"""
i   length    res
1   
"""
solution = Solution()
#A = [0,1,2,3,4,5,4,3,2,1,0]
A = [2,1,4,7,3,2,5]
#A = [1,2,0,2,0,2]
print(solution.longestMountain(A))