class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        res = 0
        d = dict()
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s not in d:
                d[s] = i
            if s == k:
                res = max(res, i+1)
            elif s-k in d:
                res = max(res, i-d[s-k])
        return res
        
