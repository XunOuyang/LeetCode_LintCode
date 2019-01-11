# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 00:24:17 2018

@author: tzlmyq
"""

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        res = int(matrix[0][0])
        dp = [[[0, 0] for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    dp[i][j] = [0, 0]
                elif i == 0 and j == 0:
                    dp[i][j] = [int(matrix[i][j]), int(matrix[i][j])]
                elif i == 0:
                    if matrix[i][j] == "1":
                        dp[i][j] = [1, dp[i][j][1] + int(matrix[i][j])]
                    else:
                        dp[i][j] = [0, 0]
                elif j == 0:
                    if matrix[i][j] == "1":
                        dp[i][j] = [dp[i][j][1] + int(matrix[i][j]), 1]
                    else:
                        dp[i][j] = [0, 0]
                else:
                    dp[i][j][0] = dp[i-1][j][0] + 1
                    dp[i][j][1] = dp[i][j-1][1] + 1
                res = max(res, dp[i][j][0] * dp[i][j][1])
        print dp
        return res
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
solution = Solution()
print solution.maximalRectangle(matrix)