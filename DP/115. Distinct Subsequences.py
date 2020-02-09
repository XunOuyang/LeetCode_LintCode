"""
https://leetcode.com/problems/distinct-subsequences/discuss/37316/7-10-lines-C++-Solutions-with-Detailed-Explanations-(O(m*n)-time-and-O(m)-space)

Genneral case 1: when s[i] == t[j]: dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
Genneral case 2: when s[i] != t[j]: dp[i][j] = dp[i-1][j]
Corner case 1: An empty string will have exactly one subsequence in any string 
    for i in range(len(s)):
            dp[i][0] = 1
Corner case 2: Non-empty string will have no subsequences in an empty string
    for j in range(len(t)):
            dp[0][j] = 0

"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        """
        dp[i][j]: by s[i], t[j] how many matches can be found
        """
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0] = 1
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
            
