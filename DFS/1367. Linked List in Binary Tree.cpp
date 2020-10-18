// 这道题有两个需要注意的点：
// 1. dfs 与 isSubPath 的recursion不一样。想想这里面的逻辑，为什么不一样呢。因为如果用一样函数去call，那么就可能，linked list中间断开了，两头存在于树中，依然相等。
// 2. 这道题，特别需要注意第20行的写法，&& 后面那个括号特别重要！

class Solution {
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        if(!head)
            return true;
        if(!root)
            return false;
        return dfs(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }
private:
    bool dfs(ListNode* head, TreeNode* root) {
        if(!head)
            return true;
        if(!root)
            return false;
        return head->val == root->val && (dfs(head->next, root->left) || dfs(head->next, root->right));
    }   
};
