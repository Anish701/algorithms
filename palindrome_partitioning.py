from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        def dfs(start, i):
            if i >= len(s):
                if i == start:
                    res.append(cur.copy())
                return

            if isPalindrome(s[start:i+1]):
                cur.append(s[start:i+1])
                dfs(i+1, i+1)
                cur.pop()

            dfs(start, i + 1)
        
        dfs(0, 0)
        return res