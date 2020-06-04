class StockSpanner:
    def __init__(self):
        self.prices = []
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append(1)
        else:
            index = len(self.stack) - 1
            while index >= 0 and price >= self.prices[index]:
                index -= self.stack[index]
            self.stack.append(len(self.stack) - index)
        self.prices.append(price)
        return self.stack[-1]
            
