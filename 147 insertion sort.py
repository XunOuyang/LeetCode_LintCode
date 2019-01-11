# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:00:49 2018

@author: tzlmyq
"""

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        
        

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre = DummyNode = ListNode(0)
        current = DummyNode.next = head
        while current and current.next:
            if current.val < current.next.val:
                current = current.next
                continue
            pre = DummyNode
            
            while pre.next.val < current.next.val:
                pre = pre.next
            temp = current.next
            current.next = temp.next
            
            # in the next step, pre.next != current
            temp.next = pre.next
            pre.next = temp
            
        pre = DummyNode.next
        while pre:
            print pre.val
            pre = pre.next
        return DummyNode.next
    
    
a = ListNode(4)
b = ListNode(3)
c = ListNode(1)
d = ListNode(2)
a.next = b
b.next = c
c.next = d
solution = Solution()
solution.insertionSortList(a)
print 
            
    
    