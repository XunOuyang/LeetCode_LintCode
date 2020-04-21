class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == (int(n**0.5))**2:
            return 1
        stack = []
        counter = 1
        for i in range(1, int(n**0.5)+1):
            stack.append(i**2)
        base = stack[:]
        visited = set(stack)
        while True:
            temp = []
            counter += 1
            for i in range(len(stack)):
                for j in range(len(base)):
                    x = stack[i] + base[j]
                    if x not in visited:
                        if x == n:
                            return counter
                        elif x < n:
                            temp.append(x)
                            visited.add(x)
            stack.extend(temp)
        return -1
