import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        length = 0
        for i in range(len(nums)):
            while q:
                if nums[q[-1]] <= nums[i]:
                    q.pop()
                elif i - q[0] >= k:
                    q.popleft()
                else:
                    break
            q.append(i)
            if i >= k-1:
                res.append(nums[q[0]])
        return res
            
                
