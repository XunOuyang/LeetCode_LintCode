# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 22:30:05 2018

@author: tzlmyq
"""

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in range(len(S)):
            print stack
            if S[i] == "(":
                stack.append("(")
            # S[i] == ")"
            else:
                # if stack[-1] == "(" 
                if not isinstance(stack[-1], int):
                    stack.pop()
                    stack.append(1)
                    while len(stack) >= 2:
                        if isinstance(stack[-2], int):
                            temp = stack.pop()
                            stack.append(stack.pop() + temp)
                        else:
                            break
                # stack[-1] is int
                else:    
                    temp = stack.pop()
                    stack.pop()
                    stack.append(2 * temp)
                    while len(stack) >= 2:
                        if isinstance(stack[-2], int):
                            temp = stack.pop()
                            stack.append(stack.pop() + temp)
                        else:
                            break
        return stack[-1]
                    
    
solution = Solution()
S = "(()((())))"
print solution.scoreOfParentheses(S)