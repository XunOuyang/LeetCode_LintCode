"""
这道题有三个要点。
1.注意，subarray允许有重复的出现。这一点很关键，不然会是指数级别难度的增加。
2. Exactly K distinct integer or element, 这个时候很容易自然想到sliding window。其实不用题中的两个相减的那种方法依然可以做。
3. 这道题的helper function里面并不要求左指针最后走到尽头，想一想这是为什么。
"""

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subarraysWithAtMostKDistinct(A, K) - self.subarraysWithAtMostKDistinct(A, K - 1)
    
    def subarraysWithAtMostKDistinct(self, A, K):
        d = collections.defaultdict(int)
        left, right = 0, 0
        res, count = 0, 0
        while right < len(A):
            d[A[right]] += 1
            if d[A[right]] == 1:
                count += 1
            right += 1
            while left < right and count > K:
                d[A[left]] -= 1
                if d[A[left]] == 0:
                    count -= 1
                left += 1
            res += right - left
        return res
