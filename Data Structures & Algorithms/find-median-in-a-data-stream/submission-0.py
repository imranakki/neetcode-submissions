from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.sl = SortedList([])

    def addNum(self, num: int) -> None:
        self.sl.add(num)

    def findMedian(self) -> float:
        n = len(self.sl)
        if n & 1:
            return self.sl[n // 2]
        return (self.sl[n // 2] + self.sl[(n - 1) // 2]) / 2
        