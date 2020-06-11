"""
Iteration 解法
"""
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        d = dict()
        stack = [root]
        while True:
            new_stack = []
            for node in stack:
                if node.left:
                    d[node.left] = node
                    new_stack.append(node.left)
                if node.right:
                    d[node.right] = node
                    new_stack.append(node.right)
            if not new_stack:
                break
            else:
                stack = new_stack
        if len(stack) == 1:
            return stack[0]
        visited = set()
        while True:
            flag = True
            new_stack = []
            for node in stack:
                if d[node] not in visited:
                    new_stack.append(d[node])
                    visited.add(d[node])
            if len(new_stack) == 1:
                return new_stack[0]
            stack = new_stack

"""
Recursion解法
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root):
            if not root: 
                return 0, None
            h1, left = helper(root.left)
            h2, right = helper(root.right)
            if h1 > h2: 
                return h1 + 1, left
            if h1 < h2: 
                return h2 + 1, right
            return h1 + 1, root
        return helper(root)[1]
