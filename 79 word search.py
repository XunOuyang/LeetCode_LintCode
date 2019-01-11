# -*- coding: utf-8 -*-
"""
Created on Thu May 17 09:57:03 2018

@author: tzlmyq
"""
import copy
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if board == [] or board == [[]]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j, 0):
                    return True
        return False 
    
    def dfs(self, board, word, i, j, index):
        if index == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"      
        res = self.dfs(board, word, i + 1, j, index + 1) or self.dfs(board, word, i - 1, j, index + 1) or self.dfs(board, word, i, j + 1, index + 1) or self.dfs(board, word, i, j - 1, index + 1)
        print board
        board[i][j] = tmp
        
        return res

   
board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCCED"


solution = Solution()
print solution.exist(board, word)
     
        
""" 
This is the wrong solution, because it is not a DFS !!! does not implement backtrack
        if board == [] or board == [[]]:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                new_board = copy.deepcopy(board)
                if self.dfs(new_board, word, i, j, 0):
                    return True
                print board
        return False 
    
    def dfs(self, board, word, i, j, index):
        if index == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[index]:
            return False
        board[i][j] = "#"        
        return self.dfs(board, word, i + 1, j, index + 1) or self.dfs(board, word, i - 1, j, index + 1) or self.dfs(board, word, i, j + 1, index + 1) or self.dfs(board, word, i, j - 1, index + 1)
"""
 