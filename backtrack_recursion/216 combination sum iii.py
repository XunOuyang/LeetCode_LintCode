"""
This problem can be solved by the template easily. 

"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(k, 1, n, [], res)
        return res
    
    def backtrack(self, k, index, n, path, res):
        if n == 0 and k == 0:
            res.append(path)
            return
        if n < 0 or k < 0:
            return
        for i in range(index, 10):
            self.backtrack(k-1, i+1, n - i, path+[i], res)
