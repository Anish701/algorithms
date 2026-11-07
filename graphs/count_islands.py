from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c):
            if (r, c) in visited or r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
                return
            
            visited.add((r,c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited or grid[r][c] == '0':
                    continue
                dfs(r, c)
                count += 1

        return count
