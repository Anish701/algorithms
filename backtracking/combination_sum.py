from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []
        subset: List[int] = [] 
        nums = sorted(nums)

        def dfs(i: int, total: int):
            if total == target:
                res.append(subset.copy())
                return
            
            for index in range(i, len(nums)):
                if total + nums[index] > target:
                    return
                subset.append(nums[index])
                dfs(index, total + nums[index])
                subset.pop()
        
        dfs(0, 0)
        return res
