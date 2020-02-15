

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.backtrack(candidates, 0, [], target, res)
        return res
    
    def backtrack(self, candidates, index, path, target, res):
        if target == 0:
            res.append(path)
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i-1] == candidates[i]:
                continue
            self.backtrack(candidates, i+1, path+[candidates[i]], target-candidates[i], res)
            """
            The difference between this problem and the problem 39 is that. 39 allows us to use same number multiple times.
            And here, all the number can be used only once. That`s why we will have 
            self.backtrack(candidates, i+1 ... ) instead of self.backtrack(candidates, i ... )
            what was more, in this problem, there could be duplicates in the candidates,
            so in order to eliminate duplicates. we need to use i > index and candidates[i-1] == candidates[i]
            it is not hard to understand that we need to use candidates[i-1] == candidates[i]. But why i > index instead of 
            i > 0 ? when i == index, path is not empty. but when i > index, path could be empty, and duplicate exist.
            """
            if i > index and candidates[i-1] == candidates[i]:
                continue
            """
            is needed
            """
