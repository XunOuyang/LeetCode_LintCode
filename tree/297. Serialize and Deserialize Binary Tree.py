# 这道题其实要做到bug free，还挺不容易写的。难点都在哪里呢？首先要明白，serialize过去的值，不是list，而是string。不一定非要跟example里面一模一样的输出，只需要
# 最后自己deserialize的时候能够还原成一样即可。很容易会想到用deque。
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
