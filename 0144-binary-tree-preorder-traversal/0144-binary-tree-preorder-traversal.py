# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        a=[]
        def p_o(root):
            if not root:
                return None 
            a.append(root.val)
            p_o(root.left)
            p_o(root.right)
        p_o(root)
        return a
        