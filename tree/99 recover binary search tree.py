# -*- coding: utf-8 -*-
"""
Created on Mon May 14 19:06:57 2018

@author: tzlmyq
"""

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
class Solution():
    def recoverTree(self, root):
        self.firstNode = TreeNode(None)
        self.secondNode = TreeNode(None)
        self.prevNode = TreeNode(None)
        
        self.traverse(root)
        self.firstNode.val, self.secondNode.val = self.secondNode.val, self.firstNode.val
        
    def traverse(self, root):
        if root == None:
            return
        
        self.traverse(root.left)
        
        # if the fist element has been found, assign it to prevElement
        if self.firstNode == None and self.prevNode.val >= root.val:
            firstNode = self.prevNode
        
        if firstNode != None and self.prevNode.val >= root.val:
            self.secondNode = root
            
        self.prevNode = root
        
        self.traverse(root.right)
