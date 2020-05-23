"""
这种题目，套路现在很熟练了。但是，一个新思路，如何避免使用两个queue呢？使用一个size 变量就可以了。
"""
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        res = []
        if root:
            q = collections.deque([root])
            size = 1
            while q:
                temp = []
                i = 0
                new_size = 0
                while i < size:
                    node = q.popleft()
                    temp.append(node.val)
                    if node.left:
                        q.append(node.left)
                        new_size += 1
                    if node.right:
                        q.append(node.right)
                        new_size += 1
                    i += 1
                size = new_size
                res.append(temp)
        return res
