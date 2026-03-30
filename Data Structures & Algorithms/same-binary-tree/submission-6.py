# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        self.traversal(p, tree1)
        self.traversal(q, tree2)

        print(tree1, tree2)
        return tree1 == tree2
    
    def traversal(self, node, l):
        if node is None:
            l.append(0)
            return
            
        l.append(node.val)
        self.traversal(node.left, l)
        self.traversal(node.right, l)

