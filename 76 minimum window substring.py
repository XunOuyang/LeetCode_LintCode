# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 14:10:30 2018

@author: tzlmyq
"""
import collections
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(s) < len(t) or map(s.find,t).count(-1) > 0:
            return ''
        A, B = collections.Counter(t), collections.Counter()       
        left, right = 0, 0
        res = s[:]
        counter = len(t)
        while right < len(s):
            while counter and right < len(s):                
                if s[right] in A:
                    B[s[right]] += 1
                    if B[s[right]] <= A[s[right]]:
                        counter -= 1
                right += 1
            while not counter:
                if len(res) > len(s[left:right]):
                    res = s[left:right]
                if s[left] in A:
                    B[s[left]] -= 1                    
                    if B[s[left]] < A[s[left]]:
                        counter += 1
                    left += 1
                else:                    
                    left += 1
        return res    
        
solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
print solution.minWindow(s, t)