class Solution {
public:
    int res = 0;
    int longestZigZag(TreeNode* root) {
        if(root == nullptr)
            return -1;
        dfs(root, true, 0);
        dfs(root, false, 0);
        return res;
    }
    
    void dfs(TreeNode* node, bool is_left, int depth)
    {
        if(!node)
            return ;
        res = max(res, depth);
        if(is_left)
        {
            dfs(node->left, left, 1);
            dfs(node->right, !left, depth + 1);
        }
        else
        {
            dfs(node->left, left, depth + 1);
            dfs(node->right, !left, 1);
        }
    }
};
