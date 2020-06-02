class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root
