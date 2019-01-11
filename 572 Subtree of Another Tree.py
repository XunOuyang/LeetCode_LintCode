# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:04:08 2018

@author: tzlmyq
"""

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s or not t:
            return False
        stack = [s]
        res = False
        while stack:
            node = stack.pop()
            res = self.check(node, t)
            if res == True:
                return res
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res
    
    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        return (node1.val == node2.val and self.check(node1.left, node2.left) and self.check(node1.right, node2.right))
        
"""
这么写肯定是不对的啊！！！
        elif node1.val != node2.val:
            return False
        else:
            self.check(node1.left, node2.left)
            self.check(node1.right, node2.right)
            
可以这么写：
        elif node1.val != node2.val:
            return False
        else:
            return self.check(node1.left, node2.left) and self.check(node1.right, node2.right)
"""
        