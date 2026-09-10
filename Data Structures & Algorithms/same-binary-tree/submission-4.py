# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # if both trees are null
        if not p and not q:
            return True

        # only one is null
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        # once we know p and q != null and their curr values match:
            # run a recursion into the subtrees below them
            # runs the same function above on the left and right subtrees
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))