"""
这道题，一定要会三个点：
1. recursion 的implementation的方法
2. iteration 的impelemntation的方法
3. python 和 C++分别的implementation，为什么会不一样
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        res.append(path[:])
        for i in xrange(index,len(nums)):
            path.extend([nums[i]])
            self.dfs(nums, i+1, path, res)
            path.pop()
    """
    The code above is more standardized. Save as C++
    the code above equals to the code below:
    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index,len(nums)):
            self.dfs(nums, i+1, path + [nums[i]], res)
    
    """
    
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            temp = []
            for item in res:
                temp.append(item)
                temp.append(item + [num])
            res = temp
        return res
                
    
