# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 10:38:27 2018

@author: TZLMYQ
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [1]
        for i in range(1, len(s)):
            if i >= 1 and s[i-1:i+1] == "00":
                return 0
            elif i >= 1 and s[i] == "0" and s[i-1] >= "3":
                return 0
            elif s[i] == "0" and i > 1:
                dp.append(dp[i-2])
            elif s[i] == "0":
                dp.append(dp[i-1])
            elif i >= 2 and s[i-1] != "0" and s[i-1:i+1] <= "26":
                dp.append(dp[i-1]+dp[i-2])
            elif s[i-1] != "0" and s[i-1:i+1] <= "26":
                dp.append(2)
            else:
                dp.append(dp[i-1])
        return dp[-1]
    
    
solution = Solution()
s = "226"
print(solution.numDecodings(s))