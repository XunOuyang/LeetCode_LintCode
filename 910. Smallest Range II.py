# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 22:39:59 2018

@author: TZLMYQ
"""

class Solution(object):
    def smallestRangeII(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        """
        max_val, min_val = max(A), min(A)
        mid = (max_val+min_val)/2
        if max_val - min_val <= k:
            return max_val - min_val
        else:
            res = []
            new_list = []
            for num in A:
                if num>mid:
                    new_list.append(num-k)
                    res.append(num-k)
                elif num<mid:
                    res.append(num+k)
                    new_list.append(num+k)
                else:
                    res.append("#")
            if new_list == res:
                return min(max(res)-min(res), max_val-min_val)
            new_max, new_min = max(new_list), min(new_list)
            if new_max - mid > mid - new_min:
                for i in range(len(res)):
                    if res[i] =="#":
                        res[i] = mid+k
            else:
                for i in range(len(res)):
                    if res[i] =="#":
                        res[i] = mid-k
            print max_val, min_val
            return max(res)-min(res)
        """
        B = sorted(A)
        min_e, max_e = B[0], B[-1]
        ret = max_e - min_e
        for i in range(len(B)-1):
            ret = min(ret, max(max_e - K, B[i] + K) - min(min_e + K, B[i+1] - K))
        
        return ret
        
solution = Solution()
A = [8038,9111,5458,8483,5052,9161,8368,2094,8366,9164,53,7222,9284,5059,4375,2667,2243,5329,3111,5678,5958,815,6841,1377,2752,8569,1483,9191,4675,6230,1169,9833,5366,502,1591,5113,2706,8515,3710,7272,1596,5114,3620,2911,8378,8012,4586,9610,8361,1646,2025,1323,5176,1832,7321,1900,1926,5518,8801,679,3368,2086,7486,575,9221,2993,421,1202,1845,9767,4533,1505,820,967,2811,5603,574,6920,5493,9490,9303,4648,281,2947,4117,2848,7395,930,1023,1439,8045,5161,2315,5705,7596,5854,1835,6591,2553,8628]
k = 4643

"""
A = [7, 8, 8, 5, 2]
k = 4
"""
print(solution.smallestRangeII(A, k))