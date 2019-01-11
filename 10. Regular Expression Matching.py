# -*- coding: utf-8 -*-
"""
Created on Sun Jul 08 21:36:19 2018

@author: TZLMYQ
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p:
            return True
        elif len(p) - 2 * p.count("*") > len(s):
            return False
        n = len(s)
        m = len(p)
        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]
        dp[0][0] = True
        for i in range(1,m):
            dp[i+1][0] = dp[i-1][0] and p[i] == "*"
        
        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == "*":
                    dp[i+1][j+1] = dp[i-1][j+1] or dp[i][j+1]
                    if p[i-1] == "." or p[i-1] == s[j]:
                        dp[i+1][j+1] |= dp[i+1][j] 
                else:
                    dp[i+1][j+1] = dp[i][j] and (s[j] == p[i] or p[i] == ".")
        print dp
        return dp[-1][-1]
    
solution = Solution()
s = "aaa"
p = "ab*ac*a"
solution.isMatch(s, p)