class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1, num2 = [], []
        for c in a:
            num1.append(int(c))
        for c in b:
            num2.append(int(c))
        a, b = num1[::-1], num2[::-1]
        if len(a) < len(b):
            a, b = b, a
        carry = 0
        i = 0
        while i < len(b):
            if carry + a[i] + b[i] == 3:
                carry = 1
                a[i] = 1
            elif carry + a[i] + b[i] == 2:
                carry = 1
                a[i] = 0
            elif carry + a[i] + b[i] == 1:
                carry = 0
                a[i] = 1
            else:
                carry = 0
                a[i] = 0
            i += 1
        while i < len(a):
            if carry == 0:
                break
            if carry + a[i] == 2:
                carry = 1
                a[i] = 0
            elif carry + a[i] == 1:
                a[i] = 1
                carry = 0
            i += 1
        if carry == 1:
            a.append(1)
        res = ""
        for item in a:
            res += str(item)
        return res[::-1]
