"""
iteration, pretty fast
"""
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [""]
        for s in S:
            if s.isalpha():
                res = [i+j for i in res for j in (s.upper(), s.lower())]
            else:
                res = [i+s for i in res]
        return res

"""
recursion: super slow
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.helper(S, 0, "", res)
        return res
        
    def helper(self, S, index, path, res):
        if len(path) == len(S):
            res.append(path)
            return
        for i in range(index, len(S)):
            if S[i].isalpha():
                self.helper(S, i+1, path + S[i].upper(), res)
                self.helper(S, i+1, path + S[i].lower(), res)
            else:
                self.helper(S, i+1, path + S[i], res)
