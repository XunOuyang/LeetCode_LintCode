class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        res, pos, neg = 0, 0, 0
        for num in nums:
            if num == 0:
                pos, neg = 0, 0
            elif num > 0:
                pos += 1
                if neg:
                    neg += 1
            elif num < 0:                
                neg, pos = pos + 1, neg + 1
                if pos == 1:
                    pos = 0
            res = max(res, pos)
        return res
