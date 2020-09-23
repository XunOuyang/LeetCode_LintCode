"""
https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1, can2 = -1, -1
        count1, count2 = 0, 0
        for num in nums:
            if num == can1:
                count1 += 1
            elif num == can2:
                count2 += 1
            elif count1 == 0:
                can1, count1 = num, 1
            elif count2 == 0:
                can2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        count1, count2 = 0, 0
        for num in nums:
            if num == can1:
                count1 += 1
            if num == can2:
                count2 += 1
        res = []
        if count1 > len(nums) / 3:
            res.append(can1)
        if count2 > len(nums) / 3:
            res.append(can2)
        return res
