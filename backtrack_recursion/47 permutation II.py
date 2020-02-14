"""
Typical backtrack solution
When we first get this solution, we need to sort them because duplicates exist.
This problem is a little bit different then the others, in order to make sure that
there will be no duplicates, we should make use visited to mark each elements that
had been visited before. So does permutation I.
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = [False]*len(nums)
        nums.sort()
        self.backtrack(nums, [], res, visited)
        return res
    
    def backtrack(self, nums,  path, res, visited):
        
        if len(path) == len(nums):
            res.append(path)
        for i in range(len(nums)):
            if not visited[i]:
                if i>0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                self.backtrack(nums, path+[nums[i]], res, visited)
                visited[i] = False


"""
Created on Sun Jul 08 15:55:15 2018

@author: TZLMYQ
Solution 2:
Actually this is not a backtrack method, it is a recursive method
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        nums.sort()
        if nums == []:
            return []
        elif len(nums) == 1:
            return [nums]
        i = 0
        while i < len(nums):
            if i + 1 < len(nums):
                if nums[i] != nums[i + 1]:
                    m = nums[i]
                    leftNums = nums[:i] + nums[i + 1:]
                    for item in self.permuteUnique(leftNums):
                        res.append([m] + item)
                i += 1
            else:
                m = nums[i]
                leftNums = nums[:i] + nums[i + 1:]
                for item in self.permuteUnique(leftNums):
                    res.append([m] + item)
                i += 1
        return res
                
