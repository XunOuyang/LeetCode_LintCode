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
class Solution {
public:
    void flatten(TreeNode* root) {
        if(root == nullptr)
            return ;
        vector<TreeNode*> stack;
        stack.push_back(root);
        TreeNode* pre = new TreeNode(0);
        pre->right = root;
        while(!stack.empty())
        {
            TreeNode* node = stack.back();
            stack.pop_back();
            pre->right = node;
            if(node->right != nullptr)
            {
                TreeNode* temp = node->right;
                stack.push_back(temp);
                node->right = nullptr;  
            }
            if(node->left != nullptr)
            {
                node->right = node->left;
                node->left = nullptr;
                stack.push_back(node->right);
            }               
            pre = pre->right;
        }
    }
};
