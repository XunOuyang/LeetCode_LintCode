# -*- coding: utf-8 -*-
"""
Created on Wed May 23 22:14:13 2018

@author: tzlmyq
this is a google interview question:
find the predecessor ofa node in a tree, find the successor in a tree
definition:
    predecessor of a node:
        if this node does not have a left subtree, then, its predecessor is its parent
        if this node has a left subtree, then its predecessor is the right most leaf of its left subtree
    successor of a node:
        if this node does not have a right subtree, then its successor is its parent
        if this node has a right subtree, then its successor is the left most leaf of its right subtree.
"""


class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
        
def findPreSuc(root, key):
    if not root:
        return
    if root.key == key:
        if root.left is not None:
            node = root.left
            while node.right:
                node = node.right
            findPreSuc.pre = node
        if root.right is not None:
            node = root.right
            while node.left:
                node = node.left
            findPreSuc.suc = node
        return
    if root.key < key:
        findPreSuc.suc = root
        findPreSuc(root.right, key)
    else:
        findPreSuc.pre = root
        findPreSuc(root.left, key)

def insert(node , key):
    if node is None:
        return TreeNode(key)
 
    if key < node.key:
        node.left = insert(node.left, key)
 
    else:
        node.right = insert(node.right, key)
 
    return node
        
key = 65 #Key to be searched in BST
  
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 
"""
root = None
root = insert(root, 50)
insert(root, 30);
insert(root, 20);
insert(root, 40);
insert(root, 70);
insert(root, 60);
insert(root, 80);
 
# Static variables of the function findPreSuc 
findPreSuc.pre = None
findPreSuc.suc = None

findPreSuc(root, key)
 
if findPreSuc.pre is not None:
    print "Predecessor is", findPreSuc.pre.key
 
else:
    print "No Predecessor"
 
if findPreSuc.suc is not None:
    print "Successor is", findPreSuc.suc.key
else:
    print "No Successor"
            