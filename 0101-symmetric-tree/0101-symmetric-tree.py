class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:

        def sym(left, right):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            if left.val != right.val:
                return False

            a = sym(left.left, right.right)
            b = sym(left.right, right.left)

            return a and b

        return sym(root.left, root.right)