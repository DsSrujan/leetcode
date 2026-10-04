
class Solution(object):
    def maxDepth(self, root):
        def ml(root):
            if not  root:
                return 0
            return 1+max(ml(root.left),ml(root.right))
        return ml(root)