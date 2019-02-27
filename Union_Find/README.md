"""
This is a standard template for union find.
"""

"""
self.rank:
    the parameter to show each node its ranking. If a node is connected with another one, they have the same ranking.
    It`s different from the height of a tree. A node with higher rank means they got more nodes linked to this chain.
    Parents will show the root of the chain.
"""

class Union_Find(object):
    def __init__(self, N):
        
        self.rank = [0] * (N + 1)
        self.parents = [i for i in range(N + 1)]
        
    def find(self, x):
        if x != self.parents[x]:
            return self.find(self.parents[x])
        return self.parents[x]
        
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank(px) == self.rank(py):
            self.parent(py) = px
            self.rank(px) += 1
        elif self.rank(px) > self.rank(py):
            self.parent(py) = px
        else:
            self.parent(px) = py
        return True
        
        
            
