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
    ListNode* insertionSortList(ListNode* head) {
        ListNode* DummyNode = new ListNode(0);
        DummyNode->next = head;
        ListNode* pre = DummyNode, *cur = head;
        while(cur) 
        {
            if((cur->next) && (cur->next->val < cur->val))
            {
                while((pre->next) && (pre->next->val < cur->next->val))
                    pre = pre->next;
                // because cur->next is the target to be compared.
                // cur->next is the pointer.
                // we manipulate pre to get everything connected to be closed
                // we manipulate cur->next->next to move the pointer to the next element
                ListNode* temp = pre->next;
                pre->next = cur->next;
                cur->next = cur->next->next;
                pre->next->next = temp;
                pre = DummyNode;
            }
            else
                cur = cur->next;
        }
        return DummyNode->next;
    }
};
