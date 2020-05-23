# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:04:08 2018

@author: tzlmyq
"""

class Solution:
    """
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """
    def isSubtree(self, s, t):
        # Write your code here
        stack = [s]
        while stack:
            node = stack.pop()
            if self.check(node, t):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
        
    def check(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val:
            if self.check(s.left, t.left) and self.check(s.right, t.right):
                return True
        return False
        
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
        
