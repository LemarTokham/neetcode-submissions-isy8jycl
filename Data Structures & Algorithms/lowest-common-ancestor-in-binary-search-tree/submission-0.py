# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        print(root.val)
        if root.val == p.val or root.val == q.val:
            print(p.val)
            return root
        
        if p.val < root.val and q.val > root.val or q.val < root.val and p.val > root.val: # Nodes lie on either side of root
            return root
        
        if p.val and q.val < root.val:
            print("left")
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val and q.val > root.val:
            print("right")
            return self.lowestCommonAncestor(root.right, p, q)