# -*- coding: utf-8 -*-
"""
Created on Sat Apr 28 14:45:58 2018

@author: tzlmyq
"""

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
class Solution():
    def uniqueBinaryTree(self, nums):
        res = []
        if len(nums) < 1:
            return res  
        for i in range(len(nums)):
            left = self.uniqueBinaryTree(nums[:i])
            right = self.uniqueBinaryTree(nums[i+1:])
            for l in left or [None]:
                for r in right or [None]:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    res.append(root)
        return res
    
    def _uniqueBinaryTree(self, n):
        if n == 0:
            return []
        else:
            return self.uniqueBinaryTree([i+1 for i in range(n)])
    
a = Solution()
n = 5
print a._uniqueBinaryTree(n)