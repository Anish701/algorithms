from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root) -> int:
            if not root:
                return 0
            
            nonlocal res
            leftH = dfs(root.left)
            rightH = dfs(root.right)
            if abs(leftH - rightH) > 1:
                res = False
            return max(leftH, rightH) + 1

        dfs(root)
        return res