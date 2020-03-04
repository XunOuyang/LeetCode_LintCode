class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        m, n = len(A), len(B)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]
