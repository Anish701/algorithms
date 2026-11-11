from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited):
            if (r, c) in visited:
                return
            
            visited.add((r, c))
            
            dirs = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for dr, dc in dirs:
                if dr < 0 or dr >= ROWS or dc < 0 or dc >= COLS:
                    continue
                if heights[dr][dc] >= heights[r][c]:
                    dfs(dr, dc, visited)
        
        for r in range(ROWS):
            for c in range(COLS):
                # pacific
                if r == 0 or c == 0:
                    dfs(r, c, pac)
                
                # atlantic
                if r == ROWS - 1 or c == COLS - 1:
                    dfs(r, c, atl)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
