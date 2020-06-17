class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and not visited[i][j]:
                    self.bfs(board, visited, i, j)
        return
    
    def bfs(self, board, visited, i, j):
        stack = [[i, j]]
        covered = []
        flag = True
        while stack:
            [x, y] = stack.pop()
            covered.append([x, y])
            visited[x][y] = True
            if x == len(board) - 1 or x == 0 or y == len(board[0]) - 1 or y == 0:
                flag = False
            if x + 1 < len(board) and board[x+1][y] == "O" and not visited[x+1][y]:
                stack.append([x+1, y])
            if y + 1 < len(board[0]) and board[x][y+1] == "O" and not visited[x][y+1]:
                stack.append([x, y+1])
            if x - 1 >= 0 and board[x-1][y] == "O" and not visited[x-1][y]:
                stack.append([x-1, y])
            if y - 1 >= 0 and board[x][y-1] == "O" and not visited[x][y-1]:
                stack.append([x, y-1])
        if flag:
            for item in covered:
                [x, y] = item
                board[x][y] = "X"
        return 
