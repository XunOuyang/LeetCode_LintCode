# 这道题是典型的bottom up dp，通解也很容易想出来。但是初始化，第10行，还有for 循环要从最小的开始往两边走，这三个重点都需要注意。
# 自己平时练习目前都做不到bug free

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][k] + dp[k][j] + A[i] * A[j] * A[k], dp[i][j])
        return dp[0][n - 1]
                    
