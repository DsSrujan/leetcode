# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def hp(root,targetSum):
            if not root:
                return False 
            if root.left==None and root.right==None and targetSum==root.val:
                return True 
            targetSum-=root.val
            l=hp(root.left, targetSum)
            r=hp(root.right,targetSum)
            return l or r
        return hp(root,targetSum)
        