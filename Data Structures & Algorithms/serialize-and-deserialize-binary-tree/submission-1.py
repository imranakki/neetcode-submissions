# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
sys.setrecursionlimit(1 << 30)
class Codec:

    preorder_str = ""
    def preorder(self, root):
        if not root:
            return "N"

        return str(root.val) + "," + self.preorder(root.left) + "," + self.preorder(root.right)
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        return self.preorder(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(",")

        i = 0;
        def dfs():
            nonlocal i

            if val[i] == "N":
                i += 1
                return None

            root = TreeNode(int(val[i]))
            i += 1
            root.left = dfs()
            root.right = dfs()
            return root

        return dfs()

    

