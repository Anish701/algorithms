from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window; keep track of char counts
        # substring length cannot be more than k + maxFreq

        mp = defaultdict(int)
        left = maxFreq = res = 0

        for right, c in enumerate(s):
            mp[c] += 1
            maxFreq = max(maxFreq, mp[c])

            while (right - left + 1) > k + maxFreq:
                mp[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res