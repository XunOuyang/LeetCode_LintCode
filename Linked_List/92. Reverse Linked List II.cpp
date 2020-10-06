// 这道题有好几个重点
// 1. memory leakage。C++写很多的linked list都喜欢用到dummy node，那么dummy node到底应该怎么写呢？
// https://stackoverflow.com/questions/3673998/what-is-difference-between-instantiating-an-object-using-new-vs-without
// 2. 解决完memory leakage的问题之后，我们需要了解这道题的思路。先找到pre node，cur node，把cur node的下一个node挪到pre的下一个，但是，pre node不动！
// 3. 接着，继续重复着把cur node的下一个放到pre node的后面。
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode dummy = ListNode(0), *pre = &dummy, *cur;
        dummy.next = head;
        for(int i=1; i < m; i++)
        {
            pre = pre->next;
        }
        cur = pre->next;
        for(int i=0; i < n-m; i++)
        {
            ListNode* temp = pre->next;
            pre->next = cur->next;
            cur->next = cur->next->next;
            pre->next->next = temp;
        }
        return dummy.next;        
    }
};
