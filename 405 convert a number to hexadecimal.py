# -*- coding: utf-8 -*-
"""
Created on Thu May 03 21:10:52 2018

@author: TZLMYQ
"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = "0123456789abcdef"
        res = ""
        if num < 0:
            num += 2**32
        for i in range(8):
            res += base[num&15]
            num /= 16
        return res[::-1].lstrip("0")
    
solution = Solution()
num = -1
print solution.toHex(num)