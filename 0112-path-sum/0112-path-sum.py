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
        :rtype: bool"""
        def hs(root,targetSum):
            if not root:
                return False
            targetSum-=root.val
            if root.left==None and root.right==None and targetSum==0:
                return True 
            l=hs(root.left, targetSum)
            r=hs(root.right,targetSum)
            return l or r
        return hs(root,targetSum)

            
       