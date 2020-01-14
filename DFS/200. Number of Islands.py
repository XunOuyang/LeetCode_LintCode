class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    res += 1
        return res
    
    def dfs(self, grid, i, j):
        stack = [[i, j]]
        while stack:
            [x, y] = stack.pop()
            grid[x][y] = '0'
            direction = [(-1, 0), (1,0), (0,1), (0,-1)]
            for i in range(len(direction)):
                m, n = direction[i][0], direction[i][1]
                if 0<=x+m< len(grid) and 0<= y+n < len(grid[0]) and grid[x] and grid[x+m][y+n] == '1':
                    stack.append([x+m,y+n])
            
                    
