class Solution {
public:
    int countNodes(TreeNode* root) {
        if(!root)
            return 0;
        int left_h=0, right_h=0;
        TreeNode* left, *right;
        left = root;
        right = root;
        while(left) {
            left = left->left;
            left_h++;
        }
        while(right) {
            right = right->right;
            right_h++;
        }
        if(left_h == right_h) {
            return pow(2, left_h) - 1;
           // return 2^left_h - 1;
        }
        else {
            return 1 + countNodes(root->left) + countNodes(root->right);
        }        
    }
};