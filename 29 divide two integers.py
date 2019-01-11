# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 19:51:32 2018

@author: tzlmyq
"""
import time

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        
        sign = 1
        if (dividend> 0)== (divisor <0):
            sign = -1
        dividend, divisor = abs(dividend),abs(divisor)
        res = 0
        while dividend>=divisor:
            temp = divisor
            i = 1
            while dividend >= temp:
                res += i
                dividend -= temp
                temp <<= 1
                i <<= 1
                
        # if wanted to get overflow into consideration:
        # then do return min(max(-2**31, res), 2**31-1)
        return res*sign
   
        
       
    
tic = time.time()
solution = Solution()
dividend = 10

divisor = 3
print solution.divide(dividend, divisor)
toc = time.time()
print toc - tic