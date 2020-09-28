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
    vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> res;
        map<int, map<int, vector<int>>> m;
        vector<pair<TreeNode*, int>> v;
        v.push_back(make_pair(root, 0));
        int level = 0;
        while(!v.empty())
        {
            vector<pair<TreeNode*, int>> new_v;
            for(auto x:v)
            {
                TreeNode* node = x.first;
                int temp = x.second;
                m[temp][level].push_back(node->val);
                if(node->left)
                    new_v.push_back(make_pair(node->left, temp - 1));
                if(node->right)
                    new_v.push_back(make_pair(node->right, temp + 1));
            }
            v = new_v;
            level++;
            
        }
        for(auto x:m)
        {
            vector<int> temp;
            for(auto y:x.second)
            {
                sort(y.second.begin(), y.second.end());
                temp.insert(temp.end(), y.second.begin(), y.second.end());
            }
            res.push_back(temp);
        }
        return res;        
    }
};
