# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = [[root.val]] # [[root]]
        level = 0
        while q:
            arr = []
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                    arr.append(node.left.val)
                if node.right:
                    q.append(node.right)
                    arr.append(node.right.val)
                print(arr)
            if arr:
                res.append(arr)    

        return res
