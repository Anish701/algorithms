from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0

            nonlocal res
            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            res = max(res, leftHeight + rightHeight)
            return max(leftHeight, rightHeight) + 1
        
        dfs(root)
        return res
