# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        # where t is the subtree (target), and s is the original tree
        # a null target is true for anything
        if not t: 
            return True

        # order matters because by this point, we know t is not Null
        if not s:
            return False

        if self.sameTree(s, t):
            return True

        return (self.isSubtree(s.left, t) or
        self.isSubtree(s.right, t))

    def sameTree(self, s, t):
        # if s and t are both null
        if not s and not t:
            return True

        # if s and t are not empty, and have matching values
        if s and t and s.val == t.val:
            # then we can move on to checking their subtrees
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))

        # if one is empty and one is not empty
        return False

        