// 用C写这两段程序是非常不容易的。之前犯了好几个错误。
// 1. 没有initialize returnSize。
// 2. 没有给所有的分配内存。
// 3. 不是特别会用malloc。


void traverse(struct TreeNode* node, int** res, int* returnColumnSizes, int depth, int* returnSize) {
    if(!node)
        return;
    *returnSize = (depth + 1 > *returnSize) ? depth + 1 : *returnSize;
    if (!returnColumnSizes[depth]) {
        res[depth] = malloc(sizeof(int)*2001);
      }
    res[depth][returnColumnSizes[depth]++] = node->val;
    traverse(node->left, res, returnColumnSizes, depth + 1, returnSize);
    traverse(node->right, res, returnColumnSizes, depth + 1, returnSize);
}

int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes){
    int** res = malloc(sizeof(int*) * 2001);
    *returnColumnSizes = malloc(sizeof(int) * 2001);
    *returnSize = 0;
    for(int i=0; i < 2001; i++)
        (*returnColumnSizes)[i] = 0;
    traverse(root, res, *returnColumnSizes, 0, returnSize);
    return res;    
}
