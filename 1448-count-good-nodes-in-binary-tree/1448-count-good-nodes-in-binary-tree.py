# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(root, m):
            if not root:
                return 0
            c=0
            if root.val>=m:
                c=1
            n_m=max(m,root.val)
            l=good(root.left,n_m)
            r=good(root.right,n_m)
            return c+l+r
        return good(root,root.val)