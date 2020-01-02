# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = PriorityQueue()
        for listnode in lists:
            if listnode:
                q.put((listnode.val, listnode))
        Dummy = cur = ListNode(0)
        while q.qsize():
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, cur.next))
        return Dummy.next
        
        """
        sorted_list = []
        for lis in lists:
            while lis:
                sorted_list.append(lis)
                lis = lis.next
        sorted_list.sort(key=attrgetter('val'))
        #sorted_list.sort(key=lambda x:x.val)
        DummyNode = ListNode(0)
        if sorted_list:
            head = DummyNode.next = sorted_list[0]
            for i in xrange(1,len(sorted_list)):
                head.next = sorted_list[i]
                head = head.next
            return DummyNode.next
        return None
        """
