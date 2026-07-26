# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    parent = {}
    val_to_node = {}
    def dfs(self, root, p = None, depth = 0):
        if not root:
            return 
        self.val_to_node[root.val] = root
        self.parent[root.val] = (p, depth)
        self.dfs(root.left, root.val, depth + 1)
        self.dfs(root.right, root.val, depth + 1)
        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.dfs(root)
        self.parent[None] = None

        x, y = p.val, q.val

        if self.parent[x][1] > self.parent[y][1]:
            x, y = y, x

        while self.parent[x][1] != self.parent[y][1]:
            y = self.parent[y][0]

        while x != y:
            y = self.parent[y][0]
            x = self.parent[x][0]

        return self.val_to_node[x]





