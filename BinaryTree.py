
# ------- Binary Tree ------- #

# invert binary tree
def invertTree(self, root):
    if root is None:
        return None

    tmp = root.left
    root.left = root.right
    root.right = tmp

    self.invertTree(root.left)
    self.invertTree(root.left)
    return root

# is valid BST
def isValidBST(root):
    def valid(node, left, right):
        if not node:
            return True

        if not (node.val < right and node.val > left):
            return False

        return(valid(node.left, left, node.val) and valid(node.right, node.val, right))
    return valid(root, float("-inf"), float("inf"))