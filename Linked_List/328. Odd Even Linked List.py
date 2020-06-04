class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        odd = head
        dummy = even = head.next
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        odd.next = dummy
        return head
