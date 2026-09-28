# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        def ibst(root,val):
            if not root:
                return TreeNode(val)
            if val<root.val:
                root.left=ibst(root.left,val)
            else :
                root.right=ibst(root.right,val)
            return root
            
        return ibst(root, val)
        
        