class Solution(object):
    def __init__(self):
        self.pre = float('-inf')
        self.res = float('inf')
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left:
            self.getMinimumDifference(root.left)
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val            
        if root.right:
            self.getMinimumDifference(root.right)
        return self.res
