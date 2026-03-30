# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.res

    def height(self, root):
        # Base case
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        if left+right > self.res:
            self.res = left+right

        return 1 + max(left, right)