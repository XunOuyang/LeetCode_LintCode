class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root)
            return 0;
        queue<TreeNode*> q;
        q.push(root);
        int res = 1;
        while(!q.empty())
        {
            int k = q.size();
            for(int i=0; i < k; i++)
            {
                TreeNode* node = q.front();
                
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);
                q.pop();
                if(!node->left && !node->right)
                    return res;                
            }
            res++;
        }
        return res;
    }
};
