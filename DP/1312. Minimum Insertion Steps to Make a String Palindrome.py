class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s)-self.longestPalindromeSubseq(s)
    
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return s
        if s == s[::-1]:
            return len(s)
        dp = [[0 for _ in xrange(len(s))] for _ in xrange(len(s))]
        for i in xrange(len(s)-1, -1, -1):
            for j in xrange(i+1, len(s)):
                dp[i][i] = 1
                if s[i] == s[j]:
                    dp[i][j] = dp[ i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]
