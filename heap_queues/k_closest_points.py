import heapq
import math
from typing import List

class Solution:
    def dist(self, point: List[int]):
        return math.sqrt(point[0]**2 + point[1]**2)
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists: List[List[int]] = []

        for i, point in enumerate(points):
            heapq.heappush_max(dists, [self.dist(point), i])
            if len(dists) > k:
                heapq.heappop_max(dists)

        res = []
        while dists:
            index = heapq.heappop(dists)[1]
            res.append(points[index])
        
        return res
