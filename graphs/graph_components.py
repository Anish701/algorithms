from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        count = 0

        adj_list = [[] for _ in range(n)]
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in adj_list[node]:
                dfs(neighbor)
            
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1

        return count
