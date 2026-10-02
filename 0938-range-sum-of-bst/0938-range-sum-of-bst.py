# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        s=0
        def rs(root, low , high):
            nonlocal s
            if not root:
                return 0
            
            l=rs(root.left,low,high)
            r=rs(root.right,low,high)

            if root.val>=low and root.val<=high:
                s+=root.val
            return l+r
        rs(root,low,high)
        return s

        
        