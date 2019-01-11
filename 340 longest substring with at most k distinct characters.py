# -*- coding: utf-8 -*-
"""
Created on Thu Aug 09 10:37:40 2018

@author: TZLMYQ
"""

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        d = dict()
        res = ""
        left, right = 0, 0
        for i, char in enumerate(s):
            if char in d:
                d[char] += 1
                right += 1
            elif len(d) < k:
                d[char] = 1
                right += 1
            else:
                d[s[left]] -= 1
                while d[s[left]] != 0:
                    left += 1
                    d[s[left]] -= 1                    
                del d[s[left]]
                left += 1
                right += 1
                if right < len(s):
                    d[s[right]] = 1
                else:
                    break
            if len(res) < right - left:
                res = s[left:right]                
        return res
                
        
        
        
    
        
solution = Solution()
s = ""
k = 3
print solution.lengthOfLongestSubstringKDistinct(s, k)