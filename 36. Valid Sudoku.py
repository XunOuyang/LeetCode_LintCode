# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 22:02:57 2018

@author: tzlmyq
"""
import collections
class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            visited = set()
            for j in range(9):
                if board[i][j] not in "123456789.":
                    return False
                elif board[i][j] in "123456789" and board[i][j] in visited:
                    return False
                else:
                    visited.add(board[i][j])

      # check all the columns
        for i in range(9):
            visited = set()     
            for j in range(9):
                if board[j][i] not in "123456789.":
                    return False
                elif board[j][i] in "123456789" and board[j][i] in visited:
                    return False
                else:
                    visited.add(board[j][i])

      # check the square
        for m in range(0, 7, 3):
            for n in range(0, 7, 3):
                visited = set()
                count = 0
                for i in range(m, 3 + m):
                    for j in range(n, 3 + n):
                        if board[i][j] not in "123456789.":
                            return False
                        elif board[i][j] in "123456789" and board[i][j] in visited:
                            return False
                        else:
                            visited.add(board[i][j])
                        print visited,  i, j
                        count += 1
                print count
        return True
    
    
    
board = [[".",".",".",".","5",".",".","1","."],[".","4",".","3",".",".",".",".","."],[".",".",".",".",".","3",".",".","1"],["8",".",".",".",".",".",".","2","."],[".",".","2",".","7",".",".",".","."],[".","1","5",".",".",".",".",".","."],[".",".",".",".",".","2",".",".","."],[".","2",".","9",".",".",".",".","."],[".",".","4",".",".",".",".",".","."]]
"""
board = [
  [".","2","3","4","5","6","7","8","9"],
  ["1",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."],
  [".",".",".",".",".",".",".",".","."]
]
"""

solution = Solution()
print solution.isValidSudoku(board)