# a typical bfs problem

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        q = deque([[root, 1]])
        while q:
            new_q = deque()
            left, right = q[0][1], q[-1][1]
            while q:
                [node, pos] = q.popleft()
                if node.left:
                    new_q.append([node.left, 2*pos-1])
                if node.right:
                    new_q.append([node.right, 2*pos])
            res = max(res, right - left + 1)
            q = new_q
        return res
            
        
