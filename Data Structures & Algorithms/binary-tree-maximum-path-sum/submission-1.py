# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    mx = float("-inf")

    def helper(self, root):
        if not root:
            return float("-inf")

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.mx = max(
            self.mx,
            root.val,
            left,
            right,
            root.val + left,
            root.val + right,
            root.val + right + left
        )

        return max(
            root.val,
            root.val + left,
            root.val + right
        )

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = float('-inf')
        self.helper(root)
        return self.mx
        