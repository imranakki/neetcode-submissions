# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ok = True
    def helper(self, root):
        if not root:
            return 0

        lh = self.helper(root.left)
        rh = self.helper(root.right)
        self.ok &= abs(lh - rh) <= 1
        return 1 + max(lh, rh)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.ok