class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        a = node.right
        while a:
            self.stack.append(a)
            a = a.left
        return node.val
                
