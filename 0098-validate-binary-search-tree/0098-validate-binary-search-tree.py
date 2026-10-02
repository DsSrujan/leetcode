class Solution(object):
    def isValidBST(self, root):

        def validate(node, low, high):

            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            left = validate(node.left, low, node.val)
            right = validate(node.right, node.val, high)

            return left and right

        return validate(root, float('-inf'), float('inf'))