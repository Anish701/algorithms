from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        res = []

        for i in range(l):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            left = i + 1
            right = l - 1

            while left < right:
                total = nums[left] + nums[right] + nums[i]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1 

                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and right > left:
                        right -= 1
        
        return res