
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A)-1
        while left < right:
            mid = (left + right)/2
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left
        
        
class Solution2(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left, right = 0, len(A)-1
        while left <= right:
            mid = (left+right)/2
            if mid > 0 and mid <len(A)-2:
                if A[mid] < A[mid-1]:
                    right = mid-1
                elif A[mid] < A[mid+1]:
                    left = mid + 1
                else:
                    return mid
            else:
                return mid
        return left
