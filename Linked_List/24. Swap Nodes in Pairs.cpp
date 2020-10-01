// 这道题可以有一个follow up，swap k nodes
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode();
        dummy->next = head;
        ListNode* cur = head;
        ListNode* pre = dummy;
        while(cur && cur->next)
        {
            ListNode* a = cur->next;
            ListNode* b = cur->next->next;
            pre->next = a;
            a->next = cur;
            cur->next = b;            
            pre = cur;
            cur = b;
        }
        return dummy->next;
    }
};
