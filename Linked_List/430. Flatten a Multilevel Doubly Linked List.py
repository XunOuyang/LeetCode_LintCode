
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        dummy = Node(0, None, head, None)
        stack = []
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                    head.next.prev = None
                head.next = head.child
                head.child.prev = head
                head.child = None
            elif not head.next and stack:
                stack[-1].prev = head
                head.next = stack.pop()
            head = head.next
        return dummy.next
