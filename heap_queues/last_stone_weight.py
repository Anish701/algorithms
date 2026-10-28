import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nums = stones
        heapq.heapify_max(nums)

        while len(nums) > 1:
            x = heapq.heappop_max(nums)
            y = heapq.heappop_max(nums)
            if x == y:
                continue
            heapq.heappush_max(nums, x-y)
        
        return nums[0] if nums else 0
