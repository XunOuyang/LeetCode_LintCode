# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            res.append(str(node.val) if node else "#")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = [item for item in data.split(",")]
        root = TreeNode(data[0])
        q =  deque([root])
        index = 1
        while q:
            node = q.popleft()
            if data[index] != "#":
                new_node = TreeNode(int(data[index]))
                node.left = new_node
                q.append(new_node)
            index += 1
            if data[index] != "#":
                new_node = TreeNode(int(data[index]))
                node.right = new_node
                q.append(new_node)
            index += 1
        return root
                
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
