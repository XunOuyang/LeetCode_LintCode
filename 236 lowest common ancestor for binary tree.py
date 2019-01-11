# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 08:39:40 2018

@author: tzlmyq
"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or q == root or p == root:
            return root.val
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right
        return right