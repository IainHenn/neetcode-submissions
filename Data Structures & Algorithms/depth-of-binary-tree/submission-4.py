# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        left = self.traverse(node.left)
        right = self.traverse(node.right)

        return max(left, right) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        else:
            return self.traverse(root)