# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:08:26 2018

@author: TZLMYQ
"""

class Solution(object):
    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return False
        
        res = []
        self.dfs(A, [], res)
        return res != []
            
    def dfs(self, A, path, res):
        if A == []:
            return
        elif path != [] and A != [] and sum(A)/float(len(A)) == sum(path)/float(len(path)):
            res.append([path, A])
            return 
        for i in range(len(A)):
            left = A[:i] + A[i+1:]
            self.dfs(left, path+[A[i]], res)
            
            
solution = Solution()
#A = [2,0,5,6,16,12,15,12,4]
#A = [1,2,3,4,5,6,7,8]
A = [0,13,13,7,5,0,10,19,5]
#A = [5,3,11,19,2]
print(solution.splitArraySameAverage(A))