class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        self.res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j):
                    return True
        return False
    
    def dfs(self, board, word, i, j):
        if board[i][j] == word[0]:
            if len(word) == 1:
                return True
            else:
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                board[i][j] = "#"
                for direction in directions:
                    [x, y] = direction
                    if 0 <= i + x < len(board) and 0 < j + y < len(board[0]) and self.dfs(board, word[1:], i + x, j + y):
                        return True
                board[i][j] = word[0]
                return False
        else:
            return False
