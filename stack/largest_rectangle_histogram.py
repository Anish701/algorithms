from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # stores (index, height)
        maxArea = 0

        for i, h in enumerate(heights):
            startIndex = i
            while stack and stack[-1][1] > h:
                startIndex, height = stack.pop()
                area = height * (i - startIndex)
                maxArea = max(area, maxArea)
            stack.append((startIndex, h))

        while stack:
            startIndex, height = stack.pop()
            area = height * (len(heights) - startIndex)
            maxArea = max(area, maxArea)

        return maxArea