class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        num1, num2 = [], []
        while x:
            num1.append(x % 2)
            x = x // 2
        while y:
            num2.append(y % 2)
            y = y // 2
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        res = 0
        i = 0
        while i < (min(len(num1), len(num2))):
            if num1[i] != num2[i]:
                res += 1
            i += 1
        while i < len(num1):
            if num1[i] == 1:
                res += 1
            i += 1
        return res
