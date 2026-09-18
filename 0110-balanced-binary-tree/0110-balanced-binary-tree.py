# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        diff=True
        def bal(root):
            nonlocal diff
            if not root :
                return 0
            l=bal(root.left)
            r=bal(root.right)
            diff=((l-r)**2)**0.5 <=1 and diff
            return 1+max(l,r)
        bal(root)
        return diff

