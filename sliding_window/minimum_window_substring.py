from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS, countT = defaultdict(int), defaultdict(int)
        left, right = 0, 0
        
        for c in t:
            countT[c] += 1
        
        resIndex = [-1, -1]
        resLen = float('inf')
        have, need = 0, len(countT)

        for right in range(len(s)):
            c = s[right]
            countS[c] += 1

            if countS[c] == countT[c]:
                have += 1

            while have == need:
                if right - left + 1 < resLen:
                    resIndex = [left, right]
                    resLen = right - left + 1
                
                c = s[left]
                countS[c] -= 1
                if countS[c] < countT[c]:
                    have -= 1
                left += 1

        resStart, resStop = resIndex[0], resIndex[1] + 1
        return s[resStart: resStop] if resLen < float('inf') else ""