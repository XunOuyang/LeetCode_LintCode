# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 23:49:39 2018

@author: TZLMYQ
"""
class Solution:

    def largestIsland(self, grid):
        
        if not grid:
            return 0
        area = {}
        def move(x, y):
            for i, j in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                if 0 <= x+i < len(grid) and 0 <= y+j < len(grid[0]):
                    yield x+i, y+j
        def dfs(i, j, index):
            temp = 0
            grid[i][j] = index
            for x, y in move(i, j):
                if grid[x][y] == 1:
                    grid[x][y] == index
                    temp += dfs(x, y, index)
            return temp + 1
        
        index = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area[index] = dfs(i, j, index)
                    index += 1
        
        # be familiar with area.values() 
        res = max(area.values() or [0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    possible = set(grid[x][y] for x, y in move(i,j) if grid[x][y] > 1)
                    res = max(res, sum(area[index] for index in possible) + 1)
        return res
      
    
solution = Solution()
grid = [[1]]
print(solution.largestIsland(grid))
