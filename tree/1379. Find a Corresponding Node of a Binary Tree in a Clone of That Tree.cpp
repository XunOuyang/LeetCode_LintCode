/*
这道题超级简单，但是不能把题目看错啊。这道题已经给出了cloned，而不是自己需要重新build 一棵树名字叫做cloned。
*/

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        if(original == target)
            return cloned;
        if(!original)
            return nullptr;
        if(original->left)
        {
            TreeNode* left = getTargetCopy(original->left, cloned->left, target);
            if(left)
                return left;
        }
        return getTargetCopy(original->right, cloned->right, target);
    }
};
