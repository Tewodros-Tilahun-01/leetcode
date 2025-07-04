# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def bfs(node):
            if not node:
                return True
            if node.val != root.val:
                return False
            return bfs(node.left) and bfs(node.right)
        return bfs(root)

