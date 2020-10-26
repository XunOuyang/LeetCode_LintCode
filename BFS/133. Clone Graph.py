
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        m = dict()
        m[node] = Node(node.val)
        q = collections.deque()
        q.append(node)
        while q:
            temp = q.popleft()
            for nei in temp.neighbors:
                if nei not in m:
                    m[nei] = Node(nei.val)                    
                    q.append(nei)
                m[temp].neighbors.append(m[nei])
        return m[node]
            
        
