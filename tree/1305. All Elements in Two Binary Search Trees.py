# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrderTraverse(self, node, v):
        if node:
            self.inOrderTraverse(node.left, v)
            v.append(node.val)
            self.inOrderTraverse(node.right, v)
    def merge(v1, v2, res):
        v3 = []
        i, j = 0, 0
        while i < len(v1) and j < len(v2):
            if v1[i] < v2[j]:
                v3.append(v1[i])
                i += 1
            else:
                v3.append(v2[j])
                j += 1
        while i < len(v1):
            v3.append(v1[i])
            i += 1
        while j < len(v2):
            v3.append(v2[j])
            j += 1
        return v3
        
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        v1, v2, res = [], [], []
        self.inOrderTraverse(root1, v1)
        self.inOrderTraverse(root2, v2)
        res = merge(v1, v2)
        return res
