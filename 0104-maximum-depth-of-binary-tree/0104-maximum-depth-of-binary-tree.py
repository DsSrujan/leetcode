
class Solution(object):
    def maxDepth(self, root):
        def ml(root):
            if not  root:
                return 0
            l=ml(root.left)
            r=ml(root.right)

            return 1+max(l,r)
        return ml(root)