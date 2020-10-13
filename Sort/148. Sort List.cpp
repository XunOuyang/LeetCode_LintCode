 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        if(head == nullptr || head->next == nullptr)
            return head;
        ListNode* fast = head,* slow = head;
        while(fast->next && fast->next->next)
        {
            fast = fast->next->next;
            slow = slow->next;
        }
        fast = slow->next;
        slow->next = nullptr;
        ListNode* left = sortList(head);
        ListNode* right = sortList(fast);        
        return merge(left, right);      
    }
    
    ListNode* merge(ListNode* left, ListNode* right) {
        if(left == nullptr)
            return right;
        else if(right == nullptr)
            return left;
        ListNode* dummy = new ListNode(0);
        ListNode* p = dummy;
        while(left && right) {
            if(left->val < right->val) {
                p->next = left;
                left = left->next; 
            }
            else {
                p->next = right;
                right = right->next;
            }
            p = p->next;
        }
        if(left == nullptr)
            p->next = right;
        else 
            p->next = left;
        return dummy->next;
    }
};
