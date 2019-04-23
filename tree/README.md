Python:


Height of a tree:
def depth(node):
    if not node:
        return 0
    left, right = depth(node.left), depth(node.right)
    return max(left, right) + 1
    

C++:
Height of a tree:
int depth(TreeNode* root) {
    if(root == NULL)
        return 0;
    return max(root->left, root->right) + 1;
