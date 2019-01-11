# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 09:17:01 2018

@author: tzlmyq
"""
import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        new_board = [[0 for _ in range(n)] for _ in range(m)]
        def judge(x, y):
            if x >= 0 and x < m and y >= 0 and y < n and board[x][y] == 1:
                return 1
            else:
                return 0
            
        def count_cell(x, y):
            quantity = 0
            quantity += judge(x + 1, y)
            quantity += judge(x - 1, y)
            quantity += judge(x, y + 1)
            quantity += judge(x, y - 1)
            quantity += judge(x + 1, y + 1)
            quantity += judge(x - 1, y + 1)
            quantity += judge(x - 1, y - 1)
            quantity += judge(x + 1, y - 1)
            return quantity
        
        for x in range(m):
            for y in range(n):
                if count_cell(x, y) > 3 or count_cell(x, y) < 2:
                    new_board[x][y] = 0
                elif count_cell(x, y) == 3:
                    new_board[x][y] = 1     
                elif count_cell(x, y) == 2:
                    new_board[x][y] = board[x][y]
        for i in range(m):
            for j in range(n):
                board[i][j] = new_board[i][j]
        print board
                
a = Solution()
board = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
#[[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
a.gameOfLife(board)