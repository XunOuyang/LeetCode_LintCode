class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        pivot1, pivot2 = [], []
        point1, point2 = 0, 0
        while point1 < len(nums1) and point2 < len(nums2):
            if nums1[point1] == nums2[point2]:
                pivot1.append(point1)
                pivot2.append(point2)
                point1 += 1
                point2 += 1
            elif point1 < len(nums1) and point2 < len(nums2) and nums1[point1] < nums2[point2]:
                point1 += 1
            elif point1 < len(nums1) and point2 < len(nums2) and nums1[point1] > nums2[point2]:
                point2 += 1
        if not pivot1:
            return max(sum(nums1), sum(nums2))
        res += max(sum(nums1[:pivot1[0]]), sum(nums2[:pivot2[0]]))
        for i in range(len(pivot1)-1):
            res += max(sum(nums1[pivot1[i]:pivot1[i+1]]), sum(nums2[pivot2[i]:pivot2[i+1]]))
        res += max(sum(nums1[pivot1[-1]:]), sum(nums2[pivot2[-1]:]))
        return res % (10**9 + 7)
                
