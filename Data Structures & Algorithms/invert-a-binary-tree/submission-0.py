# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if not root:
            return root

        temp = root.left;
        root.left = self.helper(root.right)
        root.right = self.helper(temp)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root)