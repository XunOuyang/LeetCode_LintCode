class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B = len(nums1), len(nums2)
        if (A + B) % 2 == 0:
            return (self.findKthElement((A+B)//2, nums1, nums2) + self.findKthElement((A+B)//2-1, nums1, nums2))/2.0
        else:
            return self.findKthElement((A+B)//2, nums1, nums2)
        
    def findKthElement(self, k, nums1, nums2):
        if not nums1:
            return nums2[k]
        elif not nums2:
            return nums1[k]
        mid1, mid2 = len(nums1)//2, len(nums2)//2
        if k > mid1+mid2:
            if nums1[mid1] > nums2[mid2]:
                return self.findKthElement(k-mid2-1, nums1, nums2[mid2+1:])
            else:
                return self.findKthElement(k-mid1-1, nums1[mid1+1:], nums2)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.findKthElement(k, nums1[:mid1], nums2)
            else:
                return self.findKthElement(k, nums1, nums2[:mid2])
        
            
            
