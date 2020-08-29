```
这是一道非常好的进制转换的题目。又叫rejection sampling。假设我们需要使用randM()来表示randN()，
Implement randM() using randN() when M > N:
Step 1: Use randN() to generate randX(), where X >= M. In this problem, I use 7 * (rand7() - 1) + (rand7() - 1) to generate rand49() - 1.
Step 2: Use randX() to generate randM(). In this problem, I use rand49() to generate rand40() then generate rand10.

Note: N^b * (randN() - 1) + N^(b - 1) * (randN() - 1) + N^(b - 2) * (randN() - 1) + ... + N^0 * (randN() - 1) generates randX() - 1, where X = N^(b + 1).

reference: https://leetcode.com/problems/implement-rand10-using-rand7/discuss/150301/Three-line-Java-solution-the-idea-can-be-generalized-to-%22Implement-RandM()-Using-RandN()%22

也可以参考rejection sampling.
```
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        res = 0
        while True:
            res = (rand7() - 1) * 7 + rand7() - 1
            if res < 40:
                break
        return res % 10 + 1
