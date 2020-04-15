class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        # initialization condition
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i
        
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    # dp[i+1][j] -- remove a letter from word2
                    # dp[i][j+1] -- remove a ltter from word1
                    # dp[i][j] -- replace the letter
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
        return dp[-1][-1]
