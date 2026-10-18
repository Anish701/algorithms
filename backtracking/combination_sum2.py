from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        nums = sorted(candidates)

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            if i >= len(nums):
                return
            if total + nums[i] > target:
                return
            
            subset.append(nums[i])
            dfs(i + 1, total + nums[i])
            subset.pop()

            nxt = i + 1
            while nxt < len(nums) and nums[nxt] == nums[i]:
                nxt += 1
            dfs(nxt, total)
        
        dfs(0, 0)
        return res