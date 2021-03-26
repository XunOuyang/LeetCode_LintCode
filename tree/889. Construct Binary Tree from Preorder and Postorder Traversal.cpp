class Solution {
public:
    TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
        return helper(pre, 0, pre.size(), post, 0, post.size());
    }
    
    TreeNode* helper(vector<int>& pre, int pre_left, int pre_right, vector<int>& post, int post_left, int post_right) {
        if(pre_left >= pre_right || post_left >= post_right)
            return nullptr;
        TreeNode* root = new TreeNode(pre[pre_left]);
        if(pre_left < pre_right-1 ) {
            auto pos = find(post.begin(), post.end(), pre[pre_left + 1]);
            int dis = pos - post.begin() - post_left;
            root->left = helper(pre, pre_left + 1, pre_left + 2 + dis, post, post_left, post_left + dis + 1);
            root->right = helper(pre, pre_left + dis + 2, pre_right, post, post_left + dis + 1, post_right - 1);
        }        
        return root;
    }
};
