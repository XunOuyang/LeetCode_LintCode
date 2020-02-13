# 递归
## 递归三要素
### 1. 明白想要这个函数做什么

### 2. 寻找递归结束条件
我们必须要找出递归的结束条件，不然的话，会一直调用自己，进入无底洞。也就是说，我们需要找出当参数为啥时，递归结束，之后直接把结果返回，请注意，这个时候我们必须能根据这个参数的值，能够直接知道函数的结果是什么。

### 3. 找出函数的等价关系式
第三要素就是，我们要不断缩小参数的范围，缩小之后，我们可以通过一些辅助的变量或者操作，使原函数的结果不变。这个就有点像dynamic programming的第二步。


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

# 
check if a binary tree is balanced (to all the nodes, the depth difference between its left leave and right leave cannot exceed 1)
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

其实 permutation 用下面方法并不是很好。参考Leetcode46，47两题的解答。
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

# Subset
void recursion(vector<int>& nums, vector<int>& path, int index, vector<vector<int>>& res) {
    res.push_back(path);
    for(int i=index; i<nums.size(); i++) {
        path.push_back(nums[i]);
        backtrack(nums, path, i+1, res);
        path.pop_back();
    }
    return ;
}

递归还有非常多的应用应该是用在linked list和tree的结构中。#A backtrack template:

```
def backtrack(self, nums, index, path, res):
    if when condition meets: 
    """
    the condition can be, 
      len(nums) == 0, usually res.append(path), return 
      len(nums) == 1, usually res.append([nums])
      index == len(nums), 
      len(path) == len(nums), 
    """
      res.append(path)
        #return
    for i in range(index, len(nums)):
        do something
        """
        be careful, we don`t swap elements when we use python, we only do that in C++
        """
        self.backtrack(nums, i+1, path+nums[i], res)
```
There can be even more variance of this type of template:
## Variance 1
```
def backtrack(self, nums, path, res, visited):
```
Under this circumstance, we use visited to track what elements in nums had been used or not.
## Variance 2
```
def backtrack(self, nums, path, res, target):
``` 
Under this circumstance, we can keep updating target, to find the best result we want
## Variance 3
``` 
def backtrack(self, nums, index, path, res, target):
    if target < 0:
        return
    if target == 0:
        res.append(path)
    for i in range(index, len(path)):
        self.backtrack(nums, index, path, res, target)
        # be careful here, if the backtrack(nums, index+1, ...) it means that we cannot
        # use the same elements multiple times. but if we use index, it means that we can 
        # use the same elements multiple times.
```
## Variance 4
If we do not need a new starting point to iterate the rest nums, we do not need a loop in the 
backtrack function. Such as leetcode 301
```
def backtrack(self, nums, index, path, res, target):
    if index == len(nums):
        res.append(path)
        return
    if condition:
        self.backtrack(nums, index+1...)
    elif condition:
        self.backtrack(nums, index+1...)
    else:
        self.backtrack(nums, index+1...)
```



Be very careful about it. C++ template will be different than python template, why ?
In C++, we usually could do something like:

```
        swap(nums[i], nums[index]);
        self.backtrack();
        swap(nums[i], nums[index]);

```
This will only work in C++. Sometimes we needs to be careful when we should use the second swap.



