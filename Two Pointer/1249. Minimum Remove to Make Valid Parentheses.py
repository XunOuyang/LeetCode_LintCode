class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        match, candidate = [], []
        for i, c in enumerate(s):
            if c == "(":
                candidate.append(i)
            elif candidate and c == ")":
                match.append(candidate.pop())
                match.append(i)
        match = set(match)
        for i, c in enumerate(s):
            if c == "(" or c == ")":
                if i in match:
                    res += c
            else:
                res += c
        return res
                
