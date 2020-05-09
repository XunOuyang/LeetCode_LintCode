class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        nums = []
        for i in range(len(s)):
            nums.append(abs(ord(s[i]) - ord(t[i])))
        res = 0
        left, right = 0, 0
        cost = 0
        while right < len(s):
            cost += nums[right]
            right += 1
            while cost > maxCost and left < right:
                cost -= nums[left]
                left += 1
            res = max(right - left, res)
        return res
        
