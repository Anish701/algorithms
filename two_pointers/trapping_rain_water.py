from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
        
        return res

# first attempt, this works but not optimal:
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, 0
        res = 0

        while left < len(height) - 1:
            highestRightIndex, highestRightVal = 0, 0
            right += 1

            while right < len(height):
                if height[right] >= highestRightVal:
                    highestRightVal = height[right]
                    highestRightIndex = right
                if highestRightVal >= height[left]:
                    break
                right += 1
            
            leftWall, rightWall = height[left], highestRightVal
            right = highestRightIndex
            left += 1

            while left < right:
                res += min(leftWall, rightWall) - height[left]
                left += 1
        
        return res
