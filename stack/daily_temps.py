from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res: List[int] = [0] * len(temperatures)
        stack: List[int] = [] # [index, temp]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                res[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append([i, t])
        
        return res