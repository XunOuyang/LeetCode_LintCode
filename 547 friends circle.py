# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 09:21:37 2018

@author: TZLMYQ
"""


class Solution(object):
    def findCircleNum(self, matrix):
        res = 0
        length = len(matrix)
        visited = set()
        stack = []
        for i in range(length):
            for j in range(length):
                if matrix[i][j] == 1 and i not in visited:
                    res += 1
                    visited.add(i)
                    visited.add(j)
                    stack.append(i)
                    stack.append(j)
                    while stack:
                        index = stack.pop()
                        for x in range(length):
                            if matrix[x][index] == 1 and x not in visited:
                                visited.add(x)
                                stack.append(x)
        return res
        
        
        
        
solution = Solution()
M = [[1,1,0],
 [1,1,1],
 [0,1,1]]

print solution.findCircleNum(M)