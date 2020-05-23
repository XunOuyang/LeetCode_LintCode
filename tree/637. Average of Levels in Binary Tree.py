class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        stack = [root]
        while stack:
            count = 0
            s = 0
            temp = []
            while stack:
                node = stack.pop()
                s += node.val
                count += 1
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            res.append(s/float(count))
            stack = temp
        return res
