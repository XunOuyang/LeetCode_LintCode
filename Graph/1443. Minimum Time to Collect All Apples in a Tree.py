"""
这是一道极其好的题目。题目建模就很难，就要想到如何处理。要想到在遍历一棵树的时候，如何计算cost。
"""
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        path = collections.defaultdict(list)
        for edge in edges:
            path[edge[0]].append(edge[1])
        self.cost = 0
        def dfs(node):
            found = False
            for child in path[node]:
                if dfs(child):
                    self.cost += 2
                    found = True
            return found or hasApple[node]
        dfs(0)
        return self.cost
