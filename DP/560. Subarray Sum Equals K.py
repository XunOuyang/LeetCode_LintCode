class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = 0
        res = 0
        d = {0:1}
        for num in nums:
            s += num
            res += d.get(s-k, 0)
            d[s] = d.get(s, 0)+1
        return res
