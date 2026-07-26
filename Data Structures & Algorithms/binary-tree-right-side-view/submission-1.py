# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    elem = []
    def helper(self, root, depth = 0):
        if not root:
            return

        if len(self.elem) < depth + 1:
            self.elem.append([])

        self.elem[depth].append(root.val)
        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)

        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.elem = []
        self.helper(root)
        return [e[-1] for e in self.elem]