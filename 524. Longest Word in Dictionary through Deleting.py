# -*- coding: utf-8 -*-
"""
Created on Thu Aug 02 22:21:43 2018

@author: TZLMYQ
"""

class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x:(-len(x), x))
        for word in d:
            index = 0
            pointer = 0
            while index < len(word):
                if s[pointer:].find(word[index]) != -1:
                    pointer = s[pointer:].find(word[index]) + 1
                    index += 1
                else:
                    break
            if index == len(word):
                return word
        return None
        
      
    
solution = Solution()
s = "aewfafwafjlwajflwajflwafj"
d = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]
print solution.findLongestWord(s, d)