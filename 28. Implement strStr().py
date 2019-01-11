# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 11:04:55 2018

@author: tzlmyq
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """        
        if haystack == needle or not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1
        pattern = [0]
        for i in range(1, len(needle)):
            # this is the most important step
            j = pattern[i-1]
            while j > 0 and needle[i] != needle[j]:
                j = pattern[j-1]
            if needle[i] == needle[j]:
                pattern.append(j+1)
            else:
                pattern.append(j)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = pattern[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return (i - j + 1)
        return -1
                
                
solution = Solution()
haystack = "hello"
needle = "ll"
print solution.strStr(haystack, needle)
            