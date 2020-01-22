class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        d = dict()
        d[(r, c)] = 1
        directions = [(-2, -1),(-2, 1),(2, -1),(2, 1),(1, -2), (-1, 2),(-1, -2),(1, 2)]
        for _ in range(K):
            new_d = collections.defaultdict(int)
            for key in d:
                for direction in directions:
                    if 0 <= key[0]+direction[0] < N and 0 <= key[1]+direction[1] < N:
                        new_d[(key[0]+direction[0], key[1]+direction[1])] += d[key]*0.125
            d = new_d
        
        return sum(d[key] for key in d)
