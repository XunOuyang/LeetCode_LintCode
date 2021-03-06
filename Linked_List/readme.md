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
```
C++ template:
```
struct Node { 
    int data; 
    struct Node* next; 
    Node(int data) 
    { 
        this->data = data; 
        next = NULL; 
    } 
}; 
```
C++ template 2:
```
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
```
删除一个node:
```
# 假设被删除的node是cur.next
cur.next = cur.next.next
```


最常见的linked list的操作有两种：
1. 反转
2. 找环

#### 反转
下面看来一下反转的示意图

<img src="https://github.com/XunOuyang/LeetCode/blob/master/Linked_List/image/linked_list_reverse.gif" width="480" height="480">
