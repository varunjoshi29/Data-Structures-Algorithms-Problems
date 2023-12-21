class StockSpanner:

    def __init__(self):
        self.stack = []
        self.count = 0

    def next(self, price: int) -> int:

        while len(self.stack) > 0 and price >= self.stack[-1][0]:
            self.stack.pop()
        
        if len(self.stack) > 0:
            __, index = self.stack[-1]
            self.stack.append([price, self.count])
            self.count += 1
            return self.count - 1 - index
        else:
            self.stack.append([price, self.count])
            self.count += 1
            return self.count
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)