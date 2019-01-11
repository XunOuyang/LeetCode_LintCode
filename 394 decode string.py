# -*- coding: utf-8 -*-
"""
Created on Mon May 28 11:43:05 2018

@author: tzlmyq
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        while "[" in s:
            temp = ""
            i = 0
            while s[i] != "]":
                i += 1
            end = i + 1
            i -= 1
            while s[i] != "[":
                temp += s[i]
                i -= 1
            temp = temp[::-1]
            i -= 1
            num = ""
            while i >= 0 and s[i] in "1234567890":
                num += s[i]
                i -= 1
            i += 1
            s = s[:i] + int(num[::-1]) * (temp) + s[end:]                
        return s
    
solution = Solution()
s = "3[a2[c]]"
print solution.decodeString(s)