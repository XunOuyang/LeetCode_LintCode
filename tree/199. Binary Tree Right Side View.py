# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = collections.deque([root])
        while stack:
            temp = []
            new_stack = collections.deque()
            while stack:
                node = stack.popleft()
                temp.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                if node.right:
                    new_stack.append(node.right)
            res.append(temp[-1])
            stack = new_stack
        return res
