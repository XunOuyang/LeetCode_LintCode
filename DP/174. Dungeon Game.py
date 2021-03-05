# 其实这道题，在一开始搞清楚dp 的定义，就很容易写出通解的
class Solution:
    def calculateMinimumHP(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[-1][-1] = max(1, 1 - board[-1][-1])
        for i in range(n - 2, -1, -1):
            dp[-1][i] = max(1, dp[-1][i+1] - board[-1][i])
        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1] - board[i][-1])
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i+1][j] - board[i][j], dp[i][j+1] - board[i][j]))
        return dp[0][0]
