class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        visited=[False]*len(candidates)
        self.backtrack(candidates, 0, [], target, res)
        return res
    
    def backtrack(self, candidates, index, path, target, res):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            self.backtrack(candidates, i, path+[candidates[i]], target-candidates[i], res)
            
        
