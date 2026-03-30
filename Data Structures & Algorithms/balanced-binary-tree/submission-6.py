# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) > -1

    def height(self, root):
        if root is None:
            return 0
        
        left = self.height(root.left) # 0
        right = self.height(root.right) # 0

        print(left)
        print(right)
        
        print("break")

        if abs(left - right) > 1 or left < 0 or right < 0:
            return -1

        return 1 + max(left, right)