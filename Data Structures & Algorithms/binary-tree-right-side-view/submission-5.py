# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root]
        res = [root.val]
        while q:
            right = False
            for _ in range(len(q)):
                node = q.pop(0)
                if node.right and not right:
                    right = True
                    q.append(node.right)
                    res.append(node.right.val)
                if node.left:
                    q.append(node.left)
                    if not right:
                        res.append(node.left.val)
                        right = True

        return res


