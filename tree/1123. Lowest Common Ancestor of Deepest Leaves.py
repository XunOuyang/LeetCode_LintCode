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
