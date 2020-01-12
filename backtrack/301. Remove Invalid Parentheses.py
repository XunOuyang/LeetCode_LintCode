class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        """
        Analysis:
            this is a backtrack problem 
        """
        left, right = 0, 0
        for c in s:
            if c =="(":
                left += 1
            elif c == ")":
                if left != 0:
                    left -= 1
                else:
                    right += 1
        res = set()
        self.backtrack(s, 0, left, right, 0, "", res)
        return list(res)
    
    def backtrack(self, s, i, left, right, pair, path, res):
        if i == len(s):
            if pair == 0 and left == 0 and right == 0:
                res.add(path)
            return
        
        if s[i] == "(":
            if left > 0:
                self.backtrack(s, i+1, left-1, right, pair, path, res)
            self.backtrack(s, i+1, left, right, pair+1, path+s[i], res)
        elif s[i] == ")":
            if right > 0:
                self.backtrack(s, i+1, left, right-1, pair, path, res)
            if pair > 0:
                self.backtrack(s, i+1, left, right, pair-1, path+s[i], res)
        else:
            self.backtrack(s, i+1, left, right, pair, path+s[i], res)

