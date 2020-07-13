class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        while n:
            bits.append(n % 2)
            n //= 2
        bits = bits + (32 - len(bits)) * [0]
        res = 0
        for i, item in enumerate(bits):
            res += item * (2 ** (31 - i))
        return res
