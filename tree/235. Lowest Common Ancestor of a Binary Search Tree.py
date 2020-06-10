"""
Recursioin 解法
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        if p.val < root.val < q.val or p.val > root.val > q.val:
            return root
        if p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)

"""
Iteration 解法
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or p == root or q == root:
            return root
        if q == p:
            return p
        d = dict()
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                d[node.left] = node
                stack.append(node.left)
            if node.right:
                d[node.right] = node
                stack.append(node.right)
        visited = set()
        temp = p
        while temp in d:
            if q == d[temp]:
                return q
            visited.add(temp)
            temp = d[temp]
        temp = q
        while temp in d:
            temp = d[temp]
            if temp in visited:
                return temp
        return root
