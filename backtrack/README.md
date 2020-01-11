#A backtrack template:

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



Be very careful about it. C++ template will be different than python`s, why ?
In C++, we usually could do something like:

```
        swap(nums[i], nums[index]);
        self.backtrack();
        swap(nums[i], nums[index]);

```
This will only work in C++. Sometimes we needs to be careful when we should use the second swap.
