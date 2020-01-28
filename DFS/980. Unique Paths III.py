"""
Be careful about the ending condition of this problem
"""
class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        count = 1
        x , y = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = i, j
                elif grid[i][j] == 0:
                    count += 1
        self.res = 0
        self.backtrack(x, y, count, grid)
        return self.res
    
    def backtrack(self, x, y, count, grid):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] < 0:
            return
        if grid[x][y] == 2:
            if count == 0:
                self.res += 1
            return
        grid[x][y] = -2
        self.backtrack(x+1,y, count-1, grid)
        self.backtrack(x-1,y, count-1, grid)
        self.backtrack(x,y+1, count-1, grid)
        self.backtrack(x,y-1, count-1, grid)
        grid[x][y] = 0
                
