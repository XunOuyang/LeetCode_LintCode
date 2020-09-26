// 这道题第一反应一定要是，in order traverse.
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution1 {
public:
    void inOrderTraverse(TreeNode* node, vector<int>& v)
    {
        if(node)
        {
            inOrderTraverse(node->left, v);
            v.push_back(node->val);
            inOrderTraverse(node->right, v);                
        }
    }
    
    void merge(vector<int> v1, vector<int> v2, vector<int> & v3)
    {
        int i = 0, j = 0;
        while(i < v1.size() && j < v2.size())
        {
            if(v1[i] < v2[j])
            {
                v3.push_back(v1[i]);
                i++;
            }
            else
            {
                v3.push_back(v2[j]);
                j++;
            }
        }
        while(i < v1.size())
        {
            v3.push_back(v1[i]);
            i++;
        }
        while(j < v2.size())
        {
            v3.push_back(v2[j]);
                j++;
        }
    }
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> v1, v2;
        inOrderTraverse(root1, v1);
        inOrderTraverse(root2, v2);
        vector<int> res;
        merge(v1, v2, res);
        return res;
    }
};


class Solution2 {
public:
    void pushLeft(stack<TreeNode*> &s, TreeNode* n) {
    while (n != nullptr) 
        s.push(exchange(n, n->left));
    }
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        vector<int> res;
        stack<TreeNode*> s1, s2;
        pushLeft(s1, root1);  
        pushLeft(s2, root2);
        while (!s1.empty() || !s2.empty()) {
            stack<TreeNode*> &s = s1.empty() ? s2 : s2.empty() ? s1 : 
                s1.top()->val < s2.top()->val ? s1 : s2;
            auto n = s.top(); s.pop();
            res.push_back(n->val);
            pushLeft(s, n->right);
        }
        return res;
    }
};

// line 65 to 67 is equivalent to 
while (n != nullptr){
    s.push(n);
    n = n->left;
}

