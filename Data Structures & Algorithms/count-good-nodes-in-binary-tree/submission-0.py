# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root, mx = float("-inf")):
        if not root:
            return 0

        return int(root.val >= mx) + self.helper(root.left, max(mx, root.val)) + self.helper(root.right, max(mx, root.val))
    def goodNodes(self, root: TreeNode) -> int:
        return self.helper(root)