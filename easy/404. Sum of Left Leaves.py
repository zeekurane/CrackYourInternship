# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        def recurse(root, is_left):
            if root.left:
                recurse(root.left,True)
            if root.right:
                recurse(root.right,False)
            if is_left and root.left is None and root.right is None:
                self.ans+=root.val
        recurse(root,False)
        return self.ans