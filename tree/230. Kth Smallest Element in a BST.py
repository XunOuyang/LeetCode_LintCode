class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = 0
        self.k = k
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)


"""
错误解法如下。我们必须使用self.k这么一个全局变量而不是局部变量。原因是，因为如果用k，那么k可能出现几次都为0的状态。除非这里是C++然后传递的是地址。
"""
class WrongSolution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = 0
        self.helper(root, k)
        return self.res
    
    def helper(self, node, k):
        if not node:
            return
        self.helper(node.left, k)
        k -= 1
        if k == 0:
            self.res = node.val
            return
        if k < 0:
            return 
        self.helper(node.right, k)
