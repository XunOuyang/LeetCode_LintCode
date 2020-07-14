"""
这道题特别好，特别好的点在于，用a, b作为一个dictionary的key，如:
d = dict()
d[1, 2] = 0.5
真是神奇，以前从来不知道还可以这么用的
"""

import queue
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        d = collections.defaultdict(list)
        w = dict()
        for i, edge in enumerate(edges):
            d[edge[0]].append(edge[1])
            d[edge[1]].append(edge[0])
            w[edge[0], edge[1]] = succProb[i]
            w[edge[1], edge[0]] = succProb[i]
        p = [0] * n
        p[start] = 1
        q = queue.Queue()
        q.put(start)
        counter = 1
        while not q.empty():
            node = q.get()
            for item in d[node]:
                if p[node] * w[item, node] > p[item]:
                    p[item] = p[node] * w[item, node]
                    q.put(item)
        return p[end]
        
