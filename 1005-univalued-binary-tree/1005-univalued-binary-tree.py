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
            x ,y = True,True
            if node.right:
                if node.right.val == node.val :
                    x = bfs(node.right)
                else:
                    return False
            
            if node.left :
                if node.left.val == node.val:
                   y =  bfs(node.left)
                else:
                    return False
            return x and y
        return bfs(root)

