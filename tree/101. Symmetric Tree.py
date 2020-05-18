class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.recursion(root.left, root.right)
    
    def recursion(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.recursion(left.left, right.right) and self.recursion(left.right, right.left)
