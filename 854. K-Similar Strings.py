# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:14:09 2018

@author: TZLMYQ
"""

class Solution:
    def kSimilarity(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        A, B = list(A), list(B)
        count = 0
        i = 0
        while A != B:
            while A[i] == B[i]:
                i += 1
            j = i + 1
            while A[j] == B[j]:
                j += 1
            if A[j] == B[i]:
                A[i], A[j] = A[j], A[i]
            else:
                k = j + 1
                while k < len(B):
                    if A[k] != B[k] and A[k] == B[i]:
                        A[i], A[k] = A[k], A[i]
                        break
                    k += 1
                else:
                    A[i], A[j] = A[j], A[i]                
            count += 1
            print(count, A, B)
        return count
    
solution = Solution()
A = "abcdeabcdeabcdeabcde"
B = "aaaabbbbccccddddeeee"
print(solution.kSimilarity(A, B))