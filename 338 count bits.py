# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:33:09 2018

@author: TZLMYQ
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        i = 0
        while 2**i <= num:
            i += 1
        res = [0]
        while i > 0:
            temp = [ r + 1 for r in res]
            res += temp
            i -= 1
        return res[:num+1]
    
a = Solution()
num = 2
print a.countBits(num)