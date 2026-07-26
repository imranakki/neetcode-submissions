# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    d = 0

    def helper(self, root):
        if not root:
            return 0

        lh = self.helper(root.left)
        rh = self.helper(root.right)

        self.d = max(self.d,  1 + lh + rh)
        return 1 + max(lh, rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.d - 1