"""
Iteration Solution
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = [[0] + [node] for node in graph[0]]
        flag = True
        while flag:
            new_res = []
            flag = False
            for nodes in res:
                if nodes[-1] != len(graph) - 1:
                    for node in graph[nodes[-1]]:
                        new_res.append(nodes + [node])
                        if node != len(graph) - 1:
                            flag = True
                else:
                    new_res.append(nodes)
            res = new_res
        return res
        
"""
Recursion Solution
"""
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        self.backtrack(graph, [0], res)
        return res
    
    def backtrack(self, graph, path, res):
        if path[-1] == len(graph) - 1:
            res.append(path)
            return
        for node in graph[path[-1]]:
            self.backtrack(graph, path + [node], res)
