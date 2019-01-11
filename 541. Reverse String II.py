# -*- coding: utf-8 -*-
"""
Created on Fri Jun 01 23:08:07 2018

@author: TZLMYQ
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ""
        i = 0
        length = len(s) / k
        
        for i in range(0, length + 1, 2):
            res += s[i * k : (i + 1) * k][::-1]
            print res, i
            res += s[(i + 1) * k: (i + 2) * k]
            print res, i
        return res
    
solution = Solution()
s = "abcdefg"
k = 2
print solution.reverseStr(s, k)