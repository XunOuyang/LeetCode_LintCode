class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next or m == n:
            return head
        pointer = dummy = ListNode(0)
        dummy.next = head
        pointer.next = head
        for i in range(m-1):
            pointer = pointer.next
        pre = None
        cur = pointer.next
        for i in range(n-m+1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        pointer.next.next = cur
        pointer.next = pre
        return dummy.next
