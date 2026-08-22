from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. make a set for nums. iterate thru nums figure out if num is first in seq
        # figure out num's sequence length
        
        st = set(nums)
        maxCount = 0

        for num in nums:
            if (num - 1) in st:
                continue
                
            count = 1
            while (num + count) in st:
                count += 1
            maxCount = max(maxCount, count)

        return maxCount
        
        # 2. brute force method is to check every single num as if it is the
        # start of the sequence but this will take n^2 time and sort list
        # nums.sort()
        # maxCount = 0

        # for i in range(len(nums)):
        #     count = 1

        #     for j in range(i + 1, len(nums)):
        #         if nums[j] == nums[i] + count:
        #             count += 1
            
        #     maxCount = max(maxCount, count)

        # return maxCount