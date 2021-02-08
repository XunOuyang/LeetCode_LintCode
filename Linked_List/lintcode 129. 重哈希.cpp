class Solution {
public:
    /**
     * @param hashTable: A list of The first node of linked list
     * @return: A list of The first node of linked list which have twice size
     */    
     
    void addNode(ListNode* node, int value)
    {
        while(node->next)
        {
            node = node->next;
        }
        node->next = new ListNode(value);
    }
    
    vector<ListNode*> rehashing(vector<ListNode*> hashTable) {
        // write your code here
        
        int count = 0;
        int length = hashTable.size() * 2;
        vector<ListNode*> res(length, nullptr);
        for(ListNode* & node:hashTable)
        {
            while(node != nullptr)
            {
                if(res[(node->val + length) % length] != nullptr)
                {
                    addNode(res[(node->val + length) % length], node->val);
                }
                else
                    res[(node->val + length) % length] = new ListNode(node->val);
                node = node->next;
            }
        }
        return res;
    }
};
