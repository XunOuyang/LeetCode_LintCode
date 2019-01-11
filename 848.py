# -*- coding: utf-8 -*-
"""
Created on Sat Jun 09 21:36:03 2018

@author: tzlmyq
"""

class Solution(object):
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        res = ""
        temp = 0 
        for i in range(len(S) - 1, -1, -1):
            temp += shifts[i]
            temp = temp % 26
            if ord(S[i]) + temp < ord("z"):
                res += chr(ord(S[i]) + temp)
            else:
                res += chr(ord(S[i]) + temp - 26)
        return res[::-1]
    
solution = Solution()
S = "b"
shift = [26] 
print solution.shiftingLetters(S, shift)