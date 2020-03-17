"""
This is a problem looks pretty easy but not that easy to implement. 
The true is, we have to understand that, within a valid Binary Search Tree,
All the node`s value to the right of the current node should be smaller than
the value of the current node. Vice versa. And how can we come up with a recursion
solution? It is not easy too. 
At the end, the time complexity of this problem is O(N)
and space complexity of this problem is O(N), not constant? Why, because within a 
recursion algorithm, it will build a call stack which store the status of the recursion
call. Usually the space complexity will be the depth of the tree, and worst case, the 
depth of this tree will be O(N).
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.recursion(root, float('-inf'), float('inf'))
        
    def recursion(self, node, left, right):
        if not node:
            return True
        if node.val <= left or node.val >= right:
            return False
        if not self.recursion(node.left, left , node.val):
            return False
        if not self.recursion(node.right, node.val, right):
            return False
        return True
