class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        m = dict()
        m[head] = Node(head.val)
        cur = head        
        while cur and cur.next:
            m[cur.next] = Node(cur.next.val)
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                m[cur].random = m[cur.random]
            if cur.next:
                m[cur].next = m[cur.next]
            cur = cur.next
        return m[head]
