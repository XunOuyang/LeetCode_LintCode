
This is a standard template for union find.


self.rank:
the parameter to show each node its ranking. It reflect the depth of each node connected to the tree.

self.parent:
The root of the chain for each node.


```

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
```
        
            
