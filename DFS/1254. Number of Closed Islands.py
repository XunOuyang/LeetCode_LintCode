class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 0:
                    self.flag = True
                    self.dfs(i, j, grid)
                    res += self.flag
        return res
    
    def dfs(self, x, y, grid):
        if x == 0 or y == 0 or x == len(grid)-1 or y == len(grid[0])-1:
            self.flag = False
        grid[x][y] = 2
        if x > 0 and not grid[x-1][y]:
            self.dfs(x-1, y, grid)
        if y > 0 and not grid[x][y-1]:
            self.dfs(x, y-1, grid)
        if x < len(grid)-1 and not grid[x+1][y]:
            self.dfs(x+1, y, grid)
        if y < len(grid[0])-1 and not grid[x][y+1]:
            self.dfs(x, y+1, grid)
        return 
        
