# 递归
## 递归三要素
### 1. 明白想要这个函数做什么
### 2. 寻找递归结束条件
### 3. 找出函数的等价关系式



Example:
# Hanoi
```
void hano(char a, char b, char c, int n) {
    if (n > 0) {
        hano(a, c, b, n-1);
        move(a, c);
        hano(b, a, c, n-1);
    }
}

void move(char a, char b)
{
    cout << a << "->" << b << endl;
}
```

# Depth of a binary tree
```
int depth(struct node* root)  
{  
    if (root == NULL)  
        return 0;  
    else {  
        int lDepth = depth(root->left);  //获取左子树深度  
        int rDepth = depth(root->right); //获取右子树深度  
        return lDepth>rDepth? lDepth+1: rDepth+1; //取较大值+1即为二叉树深度  
    }  
}  
```

# check if a binary tree is balanced (to all the nodes, the depth difference between its left leave and right leave cannot exceed 1)
```
bool isBalannced(TreeNode *root)
{
    if(root == NULL)
        return True;
    int left = depth(root->left);
    int right = depth(root->right);
    if(abs(left - right) > 1)
        return False;
    return isBalanced(root->left) && isBalanced(root->right);
}
```

# Permutation

```
void recursion(vector<int>& nums, int index, vector<vector<int>>& res)
{
    if(index == nums.size())
    {
        res.push_back(nums);
        return ;
    }
    for(int i=0; i<nums.size(); i++)
    {
        swap(nums[index], nums[i]);
        recursion(nums, index+1, res);
        swap(nums[index], nums[i]);
    }
}
```

