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
class BSTIterator {
public:
    stack<TreeNode*> s;
    BSTIterator(TreeNode* root) {        
        if(root)
        {
            pushLeft(s, root);
        }        
    }
    
    void pushLeft(stack<TreeNode*>& s, TreeNode* node)
    {
        s.push(node);
        while(node->left)
        {
            s.push(node->left);
            node = node->left;
        }
    }
    
    /** @return the next smallest number */
    int next() {
        TreeNode* node = s.top();
        s.pop();
        if(node->right)
        {
            pushLeft(s, node->right);
        }
        return node->val;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !s.empty();
    }
};
