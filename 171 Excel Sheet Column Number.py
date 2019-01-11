# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 10:02:47 2018

@author: TZLMYQ
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        if not s:
            return 0
        s = s[::-1]
        for i in range(len(s)):
            res += (ord(s[i]) - ord("A") + 1) * 26 ** i
        return res
    
solution = Solution()
s = "ZY"
print solution.titleToNumber(s)