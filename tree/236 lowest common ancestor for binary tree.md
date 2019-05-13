# -*- coding: utf-8 -*-
"""
Created on Thu Jun 07 08:39:40 2018

@author: tzlmyq
"""
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or q == root or p == root:
            return root.val
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right
        return right

 ``` //C++ version
    /**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == NULL || p == root || q == root)
            return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        if(left != NULL && right != NULL)
            return root;
        else if(left == NULL)
            return right;
        else if(right == NULL)
            return left;
        return root;
    }
};
```
