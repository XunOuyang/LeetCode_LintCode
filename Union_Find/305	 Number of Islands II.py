"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """
    def numIslands2(self, n, m, operators):
        # write your code here
        def index(x, y):
            return x*m+y
        res = []
        
        uf = UnionFind(m*n)
        for operator in operators:
            x, y = operator.x, operator.y
            if not uf.isIsland[index(x, y)]:
                uf.addIsland(index(x, y))
                if x > 0 and uf.isIsland[index(x-1, y)]:
                    uf.union(index(x, y), index(x-1, y))
                if x < n-1 and uf.isIsland[index(x+1, y)]:
                    uf.union(index(x, y), index(x+1, y))
                if y > 0 and uf.isIsland[index(x, y-1)]:
                    uf.union(index(x, y), index(x, y-1))
                if y < m-1 and uf.isIsland[index(x, y+1)]:
                    uf.union(index(x, y), index(x, y+1))
            res.append(uf.count)
        return res

class UnionFind:
    def __init__(self, N):
        self.rank = [0]*(N+1)
        self.parent = [i for i in range(N)]
        self.isIsland = [0]*N
        self.count = 0
        
    def find(self, x):
        if x != self.parent[x]:
            return self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] == self.rank[py]:
            self.parent[py] = px
            self.rank[px] += 1 
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px 
        else:
            self.parent[px] = py 
        self.count -= 1
        return True
            
    def addIsland(self, x):
        self.isIsland[x] = True
        self.count += 1
        

        
            
        
    
