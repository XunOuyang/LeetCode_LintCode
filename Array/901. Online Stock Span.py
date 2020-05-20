class StockSpanner(object):

    def __init__(self):
        self.prices = []
        self.rank = []
        self.size = 0

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        index = self.size - 1
        res = 1
        while index >= 0 and price >= self.prices[index]:
            res += self.rank[index]
            index -= self.rank[index]
        self.prices.append(price)
        self.rank.append(res)
        self.size += 1
        return self.rank[-1]
