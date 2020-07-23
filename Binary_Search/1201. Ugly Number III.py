class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left, right = 0, 10 ** 18
        while left != right - 1:
            mid = left + (right - left) // 2
            if self.count(mid, a, b, c) < n:
                left = mid
            else:
                right = mid
        return right
            
    def count(self, x, a, b, c):
        ans = x // a + x // b + x // c
        ans -= x // self.lcm(a, b) + x // self.lcm(a, c) + x // self.lcm(c, b)
        ans += x // self.lcm(self.lcm(a, b), c)
        return ans
    
    def lcm(self, x, y):
        return x * y // math.gcd(x, y)
    
