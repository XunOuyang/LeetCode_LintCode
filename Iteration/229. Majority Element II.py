"""
非常好的一道题。最关键的地方在于，如何iterate dictionary！
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            elif len(d) < 2:
                d[num] = 1
            else:
                for key, value in list(d.items()):
                    d[key] -= 1
                    if d[key] == 0:
                        del d[key]
        for key in d:
            d[key] = 0
        for num in nums:
            if num in d:
                d[num] += 1
        res = []
        for key in d:
            if d[key] > len(nums) / 3:
                res.append(key)
        return res
