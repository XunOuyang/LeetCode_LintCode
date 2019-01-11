# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 09:32:42 2019

@author: TZLMYQ
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        res = ""
        if numerator*denominator<0:
            res += "-"
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(int(numerator/denominator))
        if numerator%denominator == 0:
            return res
        res += "."
        remainder = numerator%denominator
        stack = []
        s = []
        while remainder and remainder not in s:
            s.append(remainder)
            remainder *= 10
            stack.append(str(int(remainder/denominator)))
            remainder = remainder%denominator
        if not remainder:
            return res+"".join(stack)
        else:
            return res+"".join(stack[:s.index(remainder)])+"(" + "".join(stack[s.index(remainder):]) +")"
            
        