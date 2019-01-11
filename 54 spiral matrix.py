# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 08:33:06 2018

@author: TZLMYQ
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or len(matrix) == 0:
            return []
        res = []
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            
            for i in range(top, bottom):
                res.append(matrix[i][right])
             
            for i in range(right, left, -1):
                res.append(matrix[bottom][i])
              
            for i in range(bottom, top, -1):
                res.append(matrix[i][left])            
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom -1
        
        if top == bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
        elif left == right:
            for i in range(left, right + 1):
                res.append(matrix[i][left])
                
        return res
            
    
solution = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print solution.spiralOrder(matrix)