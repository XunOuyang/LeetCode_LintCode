// You have to understand the difference between "." and "->" in linked list. It would be the same for tree structure

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        if(!l1 || !l2)
            return (l1?l1:l2);
        ListNode preHead(0);
        ListNode *p = &preHead;
        int carry = 0;
        while(l1 || l2 || carry) {
            int temp = (l1?l1->val:0) + (l2?l2->val:0) + carry;
            p->next = new ListNode(temp%10);
            p = p->next;
            carry = temp/10;
            l1 = l1?l1->next:l1;
            l2 = l2?l2->next:l2;
        }
        return preHead.next;
    }
};
