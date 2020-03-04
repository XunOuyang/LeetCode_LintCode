class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return m+n-2*dp[-1][-1]
