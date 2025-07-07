# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node,parent,gParent):
            if node == None:
                return 
            nonlocal count
            if gParent % 2 == 0:
                count += node.val
            dfs(node.right,node.val,parent)
            dfs(node.left,node.val,parent)
        dfs(root,1,1)
        return count