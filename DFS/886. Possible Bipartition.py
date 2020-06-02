class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 1 or not dislikes:
            return True
        
        visited = [0] * (N + 1)
        d = collections.defaultdict(list)
        for dislike in dislikes:
            d[dislike[0]].append(dislike[1])
            d[dislike[1]].append(dislike[0])
        def dfs(index, color):
            visited[index] = color
            for item in d[index]:
                if visited[item] == color:
                    return False
                if visited[item] == 0 and not dfs(item, -color):
                    return False
            return True
        
        for i in range(1, N+1):
            if visited[i] == 0 and not dfs(i, 1):
                return False 
        return True
