# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:32:37 2018

@author: TZLMYQ
"""

import Queue
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        q = Queue.PriorityQueue()
        q.put((nums1[0]+nums2[0], 0, 0))
        res = []
        visited = set((0, 0))
        k = min(len(nums1)*len(nums2), k)
        while k and q:
            _, i, j = q.get()
            if i + 1 < len(nums1) and (i+1, j) not in visited:
                visited.add((i+1, j))
                q.put((nums1[i+1]+nums2[j], i+1, j))
                print True
            if j + 1 < len(nums2) and (i, j+1) not in visited:
                visited.add((i, j+1))
                q.put((nums1[i]+nums2[j+1], i, j+1))
            res.append([nums1[i], nums2[j]])
            k -= 1
        return res
    
    
solution = Solution()
nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(solution.kSmallestPairs(nums1, nums2, k))