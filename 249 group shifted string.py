# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 18:37:24 2018

@author: TZLMYQ
"""
# leetcode 249 group shifted string. 


class Solution(object):
    def shiftedString(self, strings):
        d = dict()
        res = []
        for string in strings:
            key = self.shifted(string)
            if key in d:
                d[key].append(string)
            else:
                d[key] = [string]
                
  #      for key, value in d.iteritems():
        for key in d:
            temp = [d[key]]
            res.append(temp)                
        return res
    
    def shifted(self, string):
        key = ""
        for i in range(1, len(string)):
            diff = int(ord(string[i]) - ord(string[i-1]))
            if diff < 0:
                diff += 26
            key += chr(diff + ord("a"))
        return key
        
strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
a = Solution()
print a.shiftedString(strings)