# -*- coding: utf-8 -*-
"""
Created on Sun May 20 12:24:20 2018

@author: tzlmyq
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # split the linked-list into 2 parts
        slow = fast = head
        if not head or not head.next:
            return head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        fast = slow
        slow = slow.next
        fast.next = None
        # reverse the linkedlist from slow        
        pre = None
        while slow:
            post = slow.next
            slow.next = pre
            pre = slow
            slow = post
        slow = pre
        
        # combine two list
        pointer = fast = head
        fast = fast.next
        while slow:                    
            pointer.next = slow
            pointer = pointer.next
            slow = slow.next
            if fast:
                fast, slow = slow, fast
        
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
z = a
while a:
    print a.val
    a = a.next
solution = Solution()
solution.reorderList(z)
while z:
    print z.val
    z = z.next