from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        def checkCell(r, c):
            nonlocal fresh
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] != 1:
                return
            
            fresh -= 1
            grid[r][c] = 2
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        mins = 0
        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()

                checkCell(r + 1, c)
                checkCell(r - 1, c)
                checkCell(r, c + 1)
                checkCell(r, c - 1)
            
            mins += 1

        if fresh > 0:
            return -1
        
        return mins
