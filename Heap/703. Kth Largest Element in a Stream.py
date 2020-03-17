import bisect
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums.sort()
        self.k = k
        self.nums = nums
        
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        bisect.insort(self.nums, val)
        return self.nums[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
