Python template:
```
class ListNode(object):
    def __init__(self,val):
        self.val = val
        self.next = None
```
特别需要注意的是，double linked list,需要定义头和尾。
```
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None
        
clas LinkedList(object):
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.pre = self.head

C++ template:
```
struct ListNode {
    int val;
    ListNode *next;
};
