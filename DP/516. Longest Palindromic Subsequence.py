class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        if s == s[::-1]:
            return len(s)
        dp = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        for i in range(len(s)):
            for j in range(len(s)):
                if s[i] == s[len(s)-j-1]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]
