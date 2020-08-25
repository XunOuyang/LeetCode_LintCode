class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        vals = [i + 1 for i in range(n)]
        return self.construct(vals)
    
    def construct(self, vals):
        if not vals:
            return [None]
        res = []
        for i in range(len(vals)):
            for left in self.construct(vals[:i]):
                for right in self.construct(vals[i+1:]):
                    node = TreeNode(vals[i])
                    node.left, node.right = left, right
                    res += [node]
        return res
