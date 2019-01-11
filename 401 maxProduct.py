# -*- coding: utf-8 -*-
"""
Created on Wed May 02 20:22:07 2018

@author: tzlmyq
"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words or len(words) < 2:
            return 0
        res = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(set(words[i] + words[j])) == len(words[i]) + len(words[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res
        
        
        
a = Solution()

words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print a.maxProduct(words)