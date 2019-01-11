# -*- coding: utf-8 -*-
"""
Created on Sat May 05 21:34:46 2018

@author: tzlmyq
"""
import time

class Solution(object):
    
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 1
        res, temp, i = 0, 0, 1
        while N > temp:
            temp += i
            if N < temp:
                break
            if i % 2 == 1:
                if N % i == 0:
                    res += 1
            else:
                if N % i == (i/2):
                    res += 1
            i += 1
        return res
 
s = time.time()
print(s)
solution = Solution()
#N = 3945298
N = 2619722
N = 1810158
N = 2119006
N = 4851418
N = 8
#"abcdddeeeeaabbbcd"
print solution.consecutiveNumbersSum(N)
e = time.time()
print(e-s)