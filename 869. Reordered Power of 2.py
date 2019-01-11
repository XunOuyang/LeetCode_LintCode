# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 21:56:14 2018

@author: TZLMYQ
"""

import itertools
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        num = str(N)
        perms = list("".join(_) for _ in itertools.permutations(num))
       
        if "0" in num:
            for item in perms:
                if item[0] != "0" and bin(int(item)).count("1") == 1:
                    return True
        else:
            for item in perms:
                if bin(int(item)).count("1") == 1:
                    return True
        return False

    
solution = Solution()
N = 153454323
N = 468645235
print solution.reorderedPowerOf2(N)