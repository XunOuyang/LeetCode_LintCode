class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        """
        Be careful when reverse a linked list and concatenate two list.
        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = slow
        slow = slow.next
        pre.next = None
        pre = None
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        slow = pre
        fast = head
        while slow:
            temp = fast.next
            fast.next = slow
            fast = slow
            slow = temp
        return head
