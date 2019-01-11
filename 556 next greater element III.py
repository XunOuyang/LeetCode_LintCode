# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 18:38:08 2018

@author: tzlmyq
"""



class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return -1
        ls = list(str(n))
        if str(n) == "".join(sorted(ls, reverse = True)):
            return -1
        else:
            for i in range(len(ls)-1, -1, -1):
                if ls[i] > ls[i-1]:
                    
                    res = "".join(ls[:i-1])
                    temp = ls[i-1]
                    left = ls[i:]
                    left.sort()
                    for j in range(len(left)):
                        if left[j] > temp:
                            temp, left[j] = left[j], temp
                            break
                    res += temp
                    res += "".join(left)
                    return int(res) if int(res) < 2**31-1 else -1
                
                
solution = Solution()
n = 12
print solution.nextGreaterElement(n)