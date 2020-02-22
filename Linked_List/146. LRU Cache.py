class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.d = dict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            node = self.d[key]
            self._delete(node)
            self.add2tail(node)
            return node.val
        return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.d:
            node = self.d[key]
            self._delete(node)
        node = Node(key, value)
        self.add2tail(node)
        self.d[key] = node
        if len(self.d) > self.capacity:
            node = self.head.next
            self._delete(node)
            del self.d[node.key]
            
    def add2tail(self, node):
        pre = self.tail.pre
        pre.next = node
        self.tail.pre = node
        node.pre = pre
        node.next = self.tail
        
    def _delete(self, node):
        prev = node.pre
        nxt = node.next
        prev.next = nxt
        nxt.pre = prev

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
