// 跟copy graph一样

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if(head == nullptr)
            return nullptr;
        unordered_map<Node*, Node*> m;
        m[head]  = new Node(head->val);
        Node* cur = head;
        while(cur && cur->next)
        {
            m[cur->next] = new Node(cur->next->val);
            m[cur]->next = m[cur->next];
            cur = cur->next;
        }
        cur = head;
        while(cur)
        {
            if(cur->random != nullptr)
                m[cur]->random = m[cur->random];
            cur = cur->next;
        }
        return m[head];
    }
};
