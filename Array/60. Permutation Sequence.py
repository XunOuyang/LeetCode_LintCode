class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        """
        1. brutal force
        2. how many possibility can be ? factorial(n)
        
        """
        res = ""
        nums = [i for i in range(1, n+1)]
        k -= 1
        while n:
            index = k/math.factorial(n-1)
            res += str(nums.pop(index))
            k = k%math.factorial(n-1)
            n -= 1
        return res
