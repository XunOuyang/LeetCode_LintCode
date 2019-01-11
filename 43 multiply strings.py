# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 17:57:40 2018

@author: TZLMYQ
"""

class Solution(object):
    def multiply(self, num1, num2):
        num1 = [int(i) for i in list(num1)[::-1]]
        num2 = [int(i) for i in list(num2)[::-1]]
        res = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += num1[i] * num2[j]
        for i in range(len(res)):
            if res[i] >= 10:
                res[i+1] += res[i]/10
                res[i] = res[i]%10
        return ("".join(map(str, res[::-1]))).lstrip("0")
    
a = Solution()
num1 = "1231"
num2 = "2323"
print a.multiply(num1, num2)