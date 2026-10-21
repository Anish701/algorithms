from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        cur = []

        dig_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i):
            if i >= len(digits):
                if cur:
                    res.append("".join(cur))
                return
            
            chars = dig_char[digits[i]]
            for char in chars:
                cur.append(char)
                dfs(i+1)
                cur.pop()
        
        dfs(0)
        return res
