from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        picked = [False] * len(nums)

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            for index, num in enumerate(nums):
                print(subset, num)
                if picked[index]:
                    continue
                subset.append(num)
                picked[index] = True
                dfs(i + 1)
                subset.pop()
                picked[index] = False

        dfs(0)
        return res
