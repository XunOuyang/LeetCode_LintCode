class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or len(nums) < 3:
            return False
        small, large = sys.maxint, sys.maxint
        for num in nums:
            if num < small:
                small = num
            elif small < num < large:
                large = num
            elif num > large:
                return True
        return False
