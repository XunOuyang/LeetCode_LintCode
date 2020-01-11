A backtrack template:

````
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
Be very careful about it. C++ template will be different than python`s, why ?
In C++, we usually could do something like:

```
        swap(nums[i], nums[index]);
        self.backtrack();
        swap(nums[i], nums[index]);

```
This will only work in C++. Sometimes we needs to be careful when we should use the second swap.
