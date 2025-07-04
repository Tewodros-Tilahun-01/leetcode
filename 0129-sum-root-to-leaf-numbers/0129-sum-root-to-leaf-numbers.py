# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(node,pro):
            if not node.left and not node.right:
                return pro + str(node.val)
            x,y = 0,0
            if node.right:
                x = int(dfs(node.right,pro + str(node.val)))
            if node.left:
                y = int(dfs(node.left , pro + str(node.val)))
            return x+y
        return  int(dfs(root,""))
            