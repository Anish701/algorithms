class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window; build array of char counts; 
        # once counts equals that of s1 return true
        # if not keep moving left to decrement and right to increment
        s1counts = [0] * 26
        s2counts = [0] * 26

        for c in s1:
            s1counts[ord(c) - ord('a')] += 1

        left, right = 0, len(s1) - 1
        for i in range(left, right):
            s2counts[ord(s2[i]) - ord('a')] += 1
        
        while right < len(s2):
            s2counts[ord(s2[right]) - ord('a')] += 1

            if s2counts == s1counts:
                return True

            s2counts[ord(s2[left]) - ord('a')] -= 1

            left += 1
            right += 1

        return False