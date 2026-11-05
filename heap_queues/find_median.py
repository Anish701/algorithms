import heapq

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if self.left and num < self.left[0]:
            heapq.heappush_max(self.left, num)
        else:
            heapq.heappush(self.right, num)

        if len(self.left) > len(self.right) + 1:
            tmp = heapq.heappop_max(self.left)
            heapq.heappush(self.right, tmp)
        
        if len(self.right) > len(self.left) + 1:
            tmp = heapq.heappop(self.right)
            heapq.heappush_max(self.left, tmp)

    def findMedian(self) -> float:
        if len(self.right) > len(self.left):
            return self.right[0]
        elif len(self.right) < len(self.left):
            return self.left[0]
        else:
            return (self.left[0] + self.right[0]) / 2
