# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.parents = collections.deque()
        self.root = root
        current = collections.deque([root])        
        level = 0
        while len(current) == 2**level:
            level += 1
            new_current = collections.deque()
            for node in current:
                if node.left:
                    new_current.append(node.left)
                if node.right:
                    new_current.append(node.right)
            if len(new_current) != 2**level:                
                length = len(new_current)//2
                while length:                
                    length -= 1
                    current.popleft()
                while new_current:
                    current.append(new_current.popleft())
                break
            else:
                current = new_current            
        while current:
            self.parents.append(current.popleft())       

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = self.parents.popleft()
        new_node = TreeNode(v)
        
        if node.left == None:
            self.parents.appendleft(node)
            node.left = new_node
        else:
            node.right = new_node
        self.parents.append(new_node)
        return node.val

    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()
