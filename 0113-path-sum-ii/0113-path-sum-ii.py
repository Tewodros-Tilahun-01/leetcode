# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:return []
        def dfs(node,total,path):
            total += node.val
            path.append(node.val)
            if total == targetSum and not node.right and not node.left:
                res.append(path)
                return 
            if node.left:
                dfs(node.left,total,path[:])
            if node.right:
                dfs(node.right,total,path[:])
        dfs(root,0,[])
        return res