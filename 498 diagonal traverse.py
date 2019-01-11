# -*- coding: utf-8 -*-
"""
Created on Mon May 07 08:48:54 2018

@author: tzlmyq
"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        # the whole ides is easy, goes from 0 to M + N -2
        res = []
        if matrix == [] or matrix == [[]]:
            return res
        
        M = len(matrix)
        N = len(matrix[0])
        flag = True
        for i in range(0, M + N - 1):
            if flag == False:
                for j in range(max(i + 1 - N, 0), min(i + 1, M )):
                    res.append(matrix[j][i - j])
                flag = True
            else:
                for j in range(max(i + 1 - M, 0), min(i + 1, N )):
                    res.append(matrix[i - j][j])
                flag = False
        return res
    
solution = Solution()
matrix = [
 [ 1, 2, 3, 4 ],
 [ 5, 6, 7, 8 ],
 [ 9, 10, 11, 12 ]
]
print solution.findDiagonalOrder(matrix)
            
                
        