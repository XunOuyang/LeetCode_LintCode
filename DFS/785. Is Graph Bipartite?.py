class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            if color[i] == 0:
                color[i] = 1
                if not self.dfs(i, color, graph):
                    return False
        return True
    
    def dfs(self, index, color, graph):
        for vertice in graph[index]:
            if color[vertice] == color[index]:        
                return False
            elif color[vertice] == 0:
                color[vertice] = -color[index]
                if not self.dfs(vertice, color, graph):
                    return False
        return True
        
        
  """ 
  This problem can also be solved by BFS
  """
  class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        color = [0 for i in range(len(graph))]
        for i in range(len(graph)):
            if color[i] == 0 and graph[i] != []:
                color[i] = 1
                q = collections.deque()
                q.append(i)
                while q:
                    index = q.popleft()
                    for vertice in graph[index]:
                        if color[vertice] == 0:
                            color[vertice] = -color[index]
                            q.append(vertice)
                        elif color[vertice] == color[index]:
                            return False                  
        return True
