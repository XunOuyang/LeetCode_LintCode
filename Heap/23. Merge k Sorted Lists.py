# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        q = PriorityQueue()
        for listnode in lists:
            if listnode:
                q.put((listnode.val, listnode))
        Dummy = cur = ListNode(0)
        while not q.empty()
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, cur.next))
        return Dummy.next
        
