## Pre-Order: Root, Left, Right
## In-Order: Left, Root, Right
## Post-Order: Left, Right, Root

Python:
```
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

Height of a tree:
```
def depth(node):
    if not node:
        return 0
    left, right = depth(node.left), depth(node.right)
    return max(left, right) + 1
```
```
C++:
Definition of a tree node:
struct TreeNode{
    int data;
    TreeNode* left;
    TreeNode* right;
    TreeNode(data){
        this->data = data;
        left = right = NULL;
    }
};
```
Height of a tree:
```
int depth(TreeNode* root) {
    if(root == NULL)
        return 0;
    return max(root->left, root->right) + 1;
````
