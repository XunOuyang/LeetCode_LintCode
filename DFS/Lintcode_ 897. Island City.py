class Solution:
    """
    @param grid: an integer matrix
    @return: an integer 
    """
    def numIslandCities(self, grid):
        # Write your code here
        self.res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = -1
                    self.dfs(grid, i, j)
        return self.res
        
    def dfs(self, grid, m, n):
        stack = [[m, n]]
        self.res += 1
        while stack:
            [i, j] = stack.pop()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for direction in directions:
                x, y = i + direction[0], j + direction[1]
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] >= 1:
                    stack.append([x, y])
                    grid[x][y] = -1
                    
                
