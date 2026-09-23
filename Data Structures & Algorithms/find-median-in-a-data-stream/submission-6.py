import heapq
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr, float(num))

    def findMedian(self) -> float:
        self.arr = sorted(self.arr)
        n = len(self.arr)
        i = n//2
        if n%2 == 1:
            return self.arr[i]
        else:
            return (self.arr[i] + self.arr[i - 1])/2
        