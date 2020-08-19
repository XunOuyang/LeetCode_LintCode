class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        d = {0:-1}
        s = 0
        res = 0
        pointer = -1
        for i, num in enumerate(nums):
            s += num
            if s - target in d and pointer <= d[s - target]:
                res += 1
                pointer = i
            d[s] = i
        return res
