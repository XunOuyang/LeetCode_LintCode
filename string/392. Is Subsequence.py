class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        index = 0
        for i, c in enumerate(s):
            while index < len(t) and t[index] != c:
                index += 1
            if index == len(t):
                return False
            if i == len(s) - 1 and index < len(t) and c == t[index]:
                return True
            index += 1
        return False
