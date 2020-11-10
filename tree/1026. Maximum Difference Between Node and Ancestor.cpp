class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root, root.val, root.val)
        return self.res        
        
    def dfs(self, node, low, high):
        if not node:
            return        
        self.res = max(self.res, node.val - low, high - node.val)        
        low = min(low, node.val)
        high = max(high, node.val)
        self.dfs(node.left, low, high)
        self.dfs(node.right, low, high)
