import heapq
from collections import deque, Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = list(count.values())
        heapq.heapify_max(maxHeap)

        q = deque() # [cnt, time ready]
        time = 0

        while maxHeap or q:
            if q and q[0][1] <= time:
                heapq.heappush_max(maxHeap, q[0][0])
                q.popleft()
            
            time += 1
            if maxHeap:
                count = heapq.heappop_max(maxHeap)
                if count > 1:
                    q.append([count - 1, time + n])
        
        return time
