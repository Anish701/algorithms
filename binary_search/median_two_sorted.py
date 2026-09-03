from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(nums1) > len(nums2):
            A, B = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = total // 2
        
        l, r = 0, len(A) - 1

        while True:
            Amid = (l + r) // 2
            Bmid = half - Amid - 2

            Aleft = A[Amid] if Amid >= 0 else float("-infinity")
            Aright = A[Amid + 1] if (Amid + 1) < len(A) else float("infinity")
            Bleft = B[Bmid] if Bmid >= 0 else float("-infinity")
            Bright = B[Bmid + 1] if (Bmid + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = Amid - 1
            else:
                l = Amid + 1