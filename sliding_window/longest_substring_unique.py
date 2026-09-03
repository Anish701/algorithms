class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window and set
        # if duplicate encountered move left pointer up and remove from set until no more duplicate
        if len(s) < 1:
            return 0
        
        start, maxLen = 0, 1
        st = set()

        for i, c in enumerate(s):
            while c in st:
                st.remove(s[start])
                start += 1
            st.add(c)
            maxLen = max(maxLen, i - start + 1)

        return maxLen