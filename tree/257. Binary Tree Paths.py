class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        res = []
        self.recursion(root, "", res)
        return res
        
    def recursion(self, node, path, res):
        if not node:
            return
        if not node.left and not node.right:
            res.append(path + str(node.val))
            return
        if node.left:
            self.recursion(node.left, path + str(node.val) + "->", res)
        if node.right:
            self.recursion(node.right, path + str(node.val) + "->", res)
