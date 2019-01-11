# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 09:42:01 2018

@author: tzlmyq
"""
import collections
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        stack = collections.deque([root])
        nodes = []
        while stack:
            new_stack = collections.deque()
            temp = []
            while stack:
                node = stack.popleft()
                if node:
                    temp.append(node.val)
                else:
                    temp.append("")
                if node.left:
                    new_stack.append(node.left)
                else:
                    new_stack.append(None)
                if node.right:
                    new_stack.append(node.right)
                else:
                    new_stack.append(None)       
                                    
            nodes.append(temp)
            stack = new_stack
        res = [["" for i in range(2**(len(nodes))-1)] for j in range(len(nodes))]
        for i in range(len(nodes)):
            for j in range(len(nodes[i])):
                if nodes[i][j] != "":
                    res[i][2**(n-i)-1] = str(nodes[i][j])
                
                    
                