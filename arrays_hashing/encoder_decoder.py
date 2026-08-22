from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += str(len(s)) + '#'
            res += s
        
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            lStr = ''
            while s[i] != '#':
                lStr += s[i]
                i += 1

            l = int(lStr)
            i += 1

            resStr = ''
            for _ in range(l):
                resStr += s[i]
                i += 1
            
            res.append(resStr)
        
        return res