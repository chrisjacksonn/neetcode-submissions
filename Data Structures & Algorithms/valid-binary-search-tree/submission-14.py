# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):

            # if the tree is null
            if not node:
                return True

            # if the immediate children don't satisfy BST
            if not (left < node.val < right):
                return False

            # recurse into the left and right tree
            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        # recursion has no restrictions
        return valid(root, float("-inf"), float("inf"))