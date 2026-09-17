class Solution(object):
    def diameterOfBinaryTree(self, root):
        diameter = 0

        def md(root):
            nonlocal diameter

            if not root:
                return 0

            l = md(root.left)
            r = md(root.right)

            diameter = max(diameter, l + r)

            return 1 + max(l, r)

        md(root)
        return diameter