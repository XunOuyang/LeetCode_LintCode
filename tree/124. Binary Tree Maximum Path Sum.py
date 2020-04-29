class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.traverse(root)
        return self.res
    
    def traverse(self, node):
        if not node:
            return 0
        left, right = self.traverse(node.left), self.traverse(node.right)
        if left < 0:
            left = 0
        if right < 0:
            right = 0
        self.res = max(self.res, node.val + left + right)
        return node.val + max(left, right)
