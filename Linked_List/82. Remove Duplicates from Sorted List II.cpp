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
