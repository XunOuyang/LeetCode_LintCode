class Solution:
    def countSubstrings(self, string: str) -> int:
        # write your code here
        res = 0
        for i in range(len(string)):
            pointer = 1
            while i - pointer >= 0 and i + pointer < len(string) and string[i-pointer] == string[i+pointer]:
                res += 1
                pointer += 1
            pointer = 0
            while i - pointer >= 0 and i + pointer + 1 < len(string) and string[i-pointer] == string[i+1+pointer]:
                res += 1
                pointer += 1
            res += 1
        return res
