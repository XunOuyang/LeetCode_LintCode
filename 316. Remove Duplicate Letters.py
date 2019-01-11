# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 08:34:47 2018

@author: tzlmyq
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(sorted(list(set(s))))
    
    
solution = Solution()
s = "adfasdf"
print solution.removeDuplicateLetters(s)
        