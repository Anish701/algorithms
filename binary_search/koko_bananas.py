from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search where left is k=1 and right is k=max
        # midpoint and figure out how many hours it will take then move left from there
        left, right = 1, max(piles)
        currK = right

        while left <= right:
            mid = left + (right - left) // 2

            time = 0
            for p in piles:
                time += -(-p // mid)

            if time > h:
                left = mid + 1
            else:
                right = mid - 1
                currK = mid

        return currK