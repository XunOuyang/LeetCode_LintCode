/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        Node* start = nullptr;
        Node* end = nullptr;
        Node* node = root;
        while(node)
        {
            if(node->left)
            {
                if(!start)
                {
                    start = end = node->left;
                }
                else
                {
                    end->next = node->left;
                    end = end->next;
                }
            }
            if(node->right)
            {
                if(!start)
                {
                    start = end = node->right;
                }
                else
                {
                    end->next = node->right;
                    end = end->next;
                }
            }
            if(node->next)
                node = node->next;
            else
            {
                node = start;
                start = nullptr;
                end = nullptr;
            }
        }
        return root;
    }
};
