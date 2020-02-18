## level order traverse. bad problem.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = collections.deque([root])
        while q:
            new_q = collections.deque() 
            flag = True
            while q:
                node = q.popleft()
                if node and flag:
                    new_q.append(node.left)
                    new_q.append(node.right)
                elif not node:
                    flag = False
                elif node:
                    return False
            if not flag:
                while new_q:
                    if new_q.pop():
                        return False
            q = new_q
        return True
            
            
