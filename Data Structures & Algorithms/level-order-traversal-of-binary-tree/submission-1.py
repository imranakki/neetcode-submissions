# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    order = []
    def dfs(self, root, depth = 0):
        if not root:
            return 

        if len(self.order) < depth + 1:
            self.order.append([])

        self.order[depth].append(root.val)
        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.order = []
        self.dfs(root)
        return self.order