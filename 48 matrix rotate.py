# -*- coding: utf-8 -*-
"""
Created on Fri May 18 18:15:20 2018

@author: tzlmyq
"""

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        print matrix
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
                
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
solution = Solution()
solution.rotate(matrix)