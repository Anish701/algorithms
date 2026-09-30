from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, left: float, right: float) -> bool:
            if not root:
                return True
            if root.val <= left or root.val >= right:
                return False
            return isValid(root.left, left, root.val) and isValid(root.right, root.val, right)
        
        return isValid(root, float('-inf'), float('inf'))

    # def isValidBST(self, root: Optional[TreeNode], leftMin: int = -10000000000, rightMax: int = 10000000000) -> bool:
    #     if root.left and (root.left.val >= root.val or root.left.val <= leftMin):
    #         return False
    #     if root.right and (root.right.val <= root.val or root.right.val >= rightMax):
    #         return False
        
    #     left = not root.left or self.isValidBST(root.left, leftMin, root.val)
    #     right = not root.right or self.isValidBST(root.right, root.val, rightMax)

    #     return left and right
