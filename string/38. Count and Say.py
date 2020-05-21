# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 23:20:58 2019

@author: TZLMYQ
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        if n < 1:
            return -1
        if n == 1:
            return "1"
        res = "1"
        while n > 1:
            temp = ""
            i = 1
            count = 1
            while i < len(res):
                if res[i] == res[i-1]:
                    count += 1
                else:
                    temp += str(count) + res[i-1]
                    count = 1
                i += 1
            temp += str(count) + res[i-1]
            n -= 1
            res = temp
        return res
