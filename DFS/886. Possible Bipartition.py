"""
这是一道很好的题目。不难想到这是一个graph的题目，也不难建立起这么一个映射关系，不难想到要用dfs。
但是难的是，dfs应该返回什么呢？dfs又应该接收什么参数呢？
"""

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        self.d = collections.defaultdict(list)
        for dislike in dislikes:
            self.d[dislike[0]].append(dislike[1])
            self.d[dislike[1]].append(dislike[0])
        self.visited = [0] * (N + 1)
        for i in range(1, N):
            if not self.visited[i] and not self.dfs(i, 1):
                return False
        return True
    
    def dfs(self, index, color):
        self.visited[index] = color
        for item in self.d[index]:
            if not self.visited[item]:
                self.dfs(item, -color)
            elif self.visited[item] == color:
                return False
        return True
