class SmallestInfiniteSet:

    def __init__(self):

        self.heap = [i for i in range(1, 1001)]
        self.set_ = set(self.heap)
        

    def popSmallest(self) -> int:
        popped = heapq.heappop(self.heap)
        self.set_.remove(popped)
        return popped

        

    def addBack(self, num: int) -> None:
        if num not in self.set_:
            heapq.heappush(self.heap, num)
            self.set_.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)