from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        output, pre_mult, post_mult = [0] * l, [0] * l, [0] * l

        pre_mult[0] = 1
        for i in range(1, l):
            pre_mult[i] = nums[i-1] * pre_mult[i-1]

        post_mult[l-1] = 1
        for i in range(l-2, -1, -1):
            post_mult[i] = nums[i+1] * post_mult[i+1]

        for i in range(l):
            output[i] = pre_mult[i] * post_mult[i]

        # print(pre_mult)
        # print(post_mult)

        return output