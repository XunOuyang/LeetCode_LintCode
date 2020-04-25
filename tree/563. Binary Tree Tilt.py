"""
这道题属于特别容易犯错的一道题。The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values.看清楚了，是sum of all left subtree node value。而不是sum of absolute value，很容易犯错来着。
"""

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.res = 0
        self.value(root)
        
        return self.res
    
    def value(self, node):
        if not node:
            return 0
        left, right = self.value(node.left), self.value(node.right)
        self.res += abs(left - right)
        return node.val + left + right
