# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        def dfs(root,path,res):
            path += str(root.val)
            if not root.left and not root.right:
                res.append(path)
                return res
            if root.left:
                dfs(root.left,path+"->",res)
            if root.right:
                dfs(root.right,path+"->",res)
            return res
        return  dfs(root,"",[])