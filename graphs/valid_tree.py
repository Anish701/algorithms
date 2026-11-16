from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]
        for node, neighbor in edges:
            adj_list[node].append(neighbor)
            adj_list[neighbor].append(node)
        
        visited = set()

        def dfs(node, parent=None):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        return dfs(0) and len(visited) == n
