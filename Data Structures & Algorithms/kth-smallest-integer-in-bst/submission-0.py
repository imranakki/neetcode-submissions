# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ordered = []

    def dfs(self, root):
        if not root:
            return None

        self.dfs(root.left)
        self.ordered.append(root.val)
        self.dfs(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ordered = []
        self.dfs(root)
        return self.ordered[k - 1]