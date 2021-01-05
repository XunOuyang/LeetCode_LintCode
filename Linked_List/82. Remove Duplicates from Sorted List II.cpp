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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* Dummy = new ListNode(0);
        Dummy->next = head;
        ListNode* temp = Dummy;
        while(temp)
        {
            if(temp->next && temp->next->next && temp->next->val == temp->next->next->val)
            {
                int value = temp->next->val;
                while(temp->next && temp->next->val == value)
                    temp->next = temp->next->next;
            }
            else
            {
                temp = temp->next;
            }
        }
        return Dummy->next;
    }
};

class Solution1 {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* pre = dummy;
        ListNode* cur = head;
        bool flag = false;
        while(cur && cur->next)
        {
            while(cur->next && cur->val == cur->next->val)
            {
                flag = true;
                cur->next = cur->next->next;
            }
            if(flag)
            {
                flag = false;
                pre->next = cur->next;
                cur = pre->next;
            }
            else
            {
                cur = cur->next;
                pre = pre->next;
            }
        }
        return dummy->next;
    }
};
