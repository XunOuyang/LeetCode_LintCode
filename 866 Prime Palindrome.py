# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 10:36:59 2018

@author: TZLMYQ
"""

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 1:
            return 2
        if N == 2 or N ==3:
            return N
        elif 8 <= N <= 11:
            return 11
        n = N
        def isPrime(x):
            if x < 2 or x % 2 == 0: return x == 2
            for i in xrange(3, int(x**0.5) + 1, 2):
                if x % i == 0: return False
            return True
        
        print isPrime(111)
        if 8 <= N <= 11: return 11
        for x in xrange(10 ** (len(str(N)) / 2), 10**5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= N and isPrime(y): return y

        """        
        length = len(str(N))
        for x in range(10**(length/2),10**5):
            n = int(str(x) + str(x)[-2::-1])
            if isPrime(n) and n >= N:
                return n
        """     
                
solution = Solution()
N = 13
print solution.primePalindrome(N)

