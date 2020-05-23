"""
Understand that the leave means a tree node without children
"""
class Solution:
    """
    @param root: t
    @return: the sum of all left leaves
    """
    def sumOfLeftLeaves(self, root):
        # Write your code here
        res = 0
        if not root:
            return res
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                if not node.left.left and not node.left.right:
                    res += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res
