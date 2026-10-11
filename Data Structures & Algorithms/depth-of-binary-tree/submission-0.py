# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

        

"""
- empty is 0, root node with no children is 1
- want to hit the bottom and start passing back up an incrementer
- so return 1 per call stack, and return the recursive incremental result, taking the max
- of left and right
"""