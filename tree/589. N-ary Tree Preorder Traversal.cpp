class Solution {
public:
    vector<int> preorder(Node* root) {
        if(!root)
            return {};
        vector<int> res;
        stack<Node*> s;
        s.push(root);
        while(!s.empty()) {
            Node* node = s.top();
            s.pop();
            res.push_back(node->val);
            int n = node->children.size();
            for(int i= n - 1; i >= 0; i--) {
                s.push(node->children[i]);
            }
        }
        return res;
    }
};
