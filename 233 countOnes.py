# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 11:14:07 2018

@author: tzlmyq
"""

class Solution(object):
    def countDigitOne(self, k):
        count, factor, n = 0, 1, k
        while n > 0:
            m = n / 10
            r = n % 10
            amount = 0
            if r == 0:
                amount = 0
            elif r > 1:
                amount = factor
            else:
                amount = k % factor + 1
            
            count += m * factor + amount
            factor *= 10
            n = n / 10
        return count
    
a = Solution()
k = 1432
print a.countDigitOne(k)