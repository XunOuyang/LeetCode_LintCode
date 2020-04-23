"""
一道非常简单的数组上操作的题目。但是我根本没有想好该怎么做，就开始一通瞎做，然后很多次test case不过之后不断修改，才最后让代码通过。非常非常不好的习惯。
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return m
        list_m, list_n = [], []
        while True:
            list_m.append(m%2)
            m //= 2
            if m == 0:
                break
        while True:
            list_n.append(n%2)
            n //= 2
            if n == 0:
                break
        if len(list_m) != len(list_n):
            return 0
        res = 0
        count = 1
        for i in range(len(list_n) - 1, -1, -1):
            if list_m[i] == list_n[i]:
                res += (2**i) * list_m[i]*list_n[i]
                count += 1
            else:
                break
        return res
