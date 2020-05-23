
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0        
        if not root:
            return self.res    
        self.depth(root)
        return self.res
        
    def depth(self, node):        
        if not node:
            return 0
        left, right = self.depth(node.left), self.depth(node.right)
        self.res = max(self.res, left + right)
        return max(left, right) + 1
