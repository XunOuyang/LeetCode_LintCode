"""
leetcode 67 add binary的follow up
"""
class Solution:
    """
    @param k: The k
    @param a: The A
    @param b: The B
    @return: The answer
    """
    def addition(self, k, a, b):
        # Write your code here
        nums1, nums2 = [], []
        for c in a:
            nums1.append(int(c))
        for c in b:
            nums2.append(int(c))
        a = nums1[::-1]
        b = nums2[::-1]
        if len(a) < len(b):
            a, b = b, a
        i = 0
        carry = 0
        while i < len(b):
            if a[i] + carry + b[i] < k:
                a[i] = a[i] + carry + b[i]
                carry = 0
            else:
                a[i] = a[i] + carry + b[i] - k
                carry = 1
            i += 1
        while i < len(a):
            if a[i] + carry < k:
                a[i] = a[i] + carry
                carry = 0
                break
            else:
                a[i] = a[i] + carry - k
                carry = 1
            i += 1
        if carry == 1:
            a.append(1)
        res = ""
        flag = False
        for num in a:
            res += str(num)
        i = len(res) - 1
        while res[i] == "0":
            i -= 1
        res = res[:i+1]
        return res[::-1]
