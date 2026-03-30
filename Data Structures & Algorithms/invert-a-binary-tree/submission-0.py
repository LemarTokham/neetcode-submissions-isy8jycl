# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def swapNodes(self, root):
        if root is None:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.swapNodes(root.left)
        self.swapNodes(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.swapNodes(root)

        return root