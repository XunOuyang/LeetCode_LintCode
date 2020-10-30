"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        # Write your code here.
        self.pre = None
        self.head = None
        self.traverse(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head
        
    def traverse(self, node):
        if node.left:
            self.traverse(node.left)
        if not self.head:
            self.head = node
            self.pre = self.head
        else:
            self.pre.right = node
            node.left = self.pre
            self.pre = self.pre.right
        if node.right:
            self.traverse(node.right)
