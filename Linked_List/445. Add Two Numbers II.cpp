// By figuring out how to do this problem, then you can deeply understand the difference between "." and "->"
// This problem is a combination of leetcode 2 Add Two Numbers and leetcode 206	Reverse Linked List

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
        ListNode* r1 = reverseList(l1);
        ListNode* r2 = reverseList(l2);
        ListNode dummy(0), *p = &dummy;
        int carry = 0;
        while(r1 || r2 || carry) {
            int temp = (r1?r1->val:0) + (r2?r2->val:0) + carry;
            p->next = new ListNode(temp%10);
            p = p->next;
            carry = temp/10;
            r1 = (r1?r1->next:r1);
            r2 = (r2?r2->next:r2);
        }
        p->next = (r1?r1:r2);
        p = reverseList(dummy.next);
        return p;
    }
    
    ListNode* reverseList(ListNode* head) {
        ListNode* pre(NULL);
        while(head) {
            ListNode* post = head->next;
            head->next = pre;
            pre = head;
            head = post;
        }
        return pre;
    }
};
