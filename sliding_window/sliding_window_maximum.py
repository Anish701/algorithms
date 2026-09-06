from typing import List
from collections import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # brute force: O(n*k)
        # res = []
        # for r in range(k - 1, len(nums)):
        #     res.append(max(nums[r - k + 1 : r + 1]))
        # return res

        # max heap with heapq using negative values: (nlogn)
        # keep removing max heap top val if not in window
        heap = []
        res = []
        
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i < k - 1:
                continue

            while heap[0][1] <= i - k:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        
        return res