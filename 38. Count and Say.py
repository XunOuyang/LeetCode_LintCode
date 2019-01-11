# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 23:20:58 2019

@author: TZLMYQ
"""

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        if n == 1:
            return res
        while n > 1:
            count = 1
            s = ""
            i = 0
            while i < len(res):
                count = 1
                while i+1 < len(res) and res[i] == res[i+1]:
                    count += 1
                    i += 1
                s += str(count) + res[i]
                i += 1
            n -= 1
            res = s
        return res