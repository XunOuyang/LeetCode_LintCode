class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i+1 for i in range(n)]
        res = []        
        self.recursion(nums, 0, [], res, k)
        return res
    
    def recursion(self, nums, index, path, res, k):
        if len(path) == k:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.recursion(nums, i+1, path+[nums[i]], res, k)
