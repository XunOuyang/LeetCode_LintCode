# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:08:36 2018

@author: tzlmyq
"""

class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack1 = []
        stack2 = []
        for item in s:
            if item == "(":
                stack1.append("(")
            elif item == "*":
                stack2.append("*")
            else:
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else:
                    return False
        return False if len(stack1) > len(stack2) else True
    
solution = Solution()
s = "(())((())()()(*)(*()(())())())()()((()())((()))(*"
print solution.checkValidString(s)