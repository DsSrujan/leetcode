# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def ml(root):
            if not  root:
                return 0
            l=ml(root.left)
            r=ml(root.right)

            return 1+max(l,r)
        return ml(root)