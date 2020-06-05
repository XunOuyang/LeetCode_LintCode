class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        res = -1
        stack = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    stack.append([i, j])
        if len(stack) == 0 or len(stack) == len(grid) * len(grid[0]):
            return res
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while stack:
            new_stack = []
            while stack:
                [i, j] = stack.pop()
                for direction in directions:
                    x, y = i + direction[0], j + direction[1]
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                        grid[x][y] = "#"
                        new_stack.append([x, y])
            stack = new_stack
            res += 1
        return res
