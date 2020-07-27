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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return createTree(inorder, postorder, 0, inorder.size() - 1, 0, postorder.size() - 1);
    }
    
    TreeNode* createTree(vector<int>& inorder, vector<int>& postorder, int is, int ie, int ps, int pe) {
        if(ps > pe)
            return nullptr;
        TreeNode *root = new TreeNode(postorder[pe]);
        int index = 0;
        for(int i=is; i <= ie; i++)
        {
            if(inorder[i] == postorder[pe])
            {
                index = i;
                break;
            }
        }
        TreeNode* left = createTree(inorder, postorder, is, index - 1, ps, ps - is + index - 1);
        TreeNode* right = createTree(inorder, postorder, index + 1, ie, ps - is + index, pe-1);
        root->left = left;
        root->right = right;
        return root;
    }
};
