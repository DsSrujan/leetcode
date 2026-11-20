# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        a=[]
        def i_t(root):
            if not root:
                return None 
            i_t(root.left)
            a.append(root.val)
            i_t(root.right)
        i_t(root)
        return a

        