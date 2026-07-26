# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
      
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], splited = False) -> bool:
        if (not root and not subRoot) :
            return True

        if (not root and subRoot) or (root and not subRoot):
            return False

        ans = False

        
        if root.val == subRoot.val:
            ans |= (self.isSubtree(root.left, subRoot.left, True) and self.isSubtree(root.right, subRoot.right, True)) 
        
        if not splited:
            ans |= self.isSubtree(root.left, subRoot, splited) or self.isSubtree(root.right, subRoot, splited)

        return ans