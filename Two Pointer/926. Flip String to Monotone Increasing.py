class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        zeros, ones = 0, 0
        flag = False
        res = 0
        for c in S:
            if c == "1":
                ones += 1
                flag = True
            elif c == "0" and flag:
                zeros += 1
                if zeros > ones:
                    res += ones
                    ones = 0
                    zeros = 0
                    flag = False
        return res + zeros
                    
