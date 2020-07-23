# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur = headA
        length_A = 0
        while cur:
            length_A += 1
            cur = cur.next
        cur = headB
        length_B = 0
        while cur:
            length_B += 1
            cur = cur.next
        if length_A > length_B:
            m = length_A - length_B
            while m:
                m -= 1
                headA = headA.next
        else:
            m = length_B - length_A
            while m:
                m -= 1
                headB = headB.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
