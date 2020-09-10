// 不得不说，lee这哥们太强了。。。
class Solution {
public:
    int res = 0;
    int sumRootToLeaf(TreeNode* root, int val = 0) {
        if(!root)
            return 0;
        val = val * 2 + root->val;
        return !root->left && !root->right ? val:sumRootToLeaf(root->left, val) + sumRootToLeaf(root->right, val);
    }        
};
