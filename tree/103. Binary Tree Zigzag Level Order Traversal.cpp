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
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        vector<TreeNode*> stack;
        if(root)
            stack.push_back(root);
        bool flag = true;
        while(!stack.empty())
        {
            vector<TreeNode*> temp;
            vector<int> res_row;
            if(flag)
            {
                for(int i=stack.size()-1; i >= 0; i--)
                {
                    res_row.push_back(stack[i]->val);
                    if(stack[i]->left != nullptr)
                        temp.push_back(stack[i]->left);
                    if(stack[i]->right != nullptr)
                        temp.push_back(stack[i]->right);
                }
                res.push_back(res_row);
                flag = false;
            }
            else
            {
                for(int i=stack.size()-1; i >= 0; i--)
                {
                    res_row.push_back(stack[i]->val);
                    if(stack[i]->right != nullptr)
                        temp.push_back(stack[i]->right);
                    if(stack[i]->left != nullptr)
                        temp.push_back(stack[i]->left);
                }
                res.push_back(res_row);
                flag = true;
            }
            stack = temp;
        }
        return res;
    }
};
