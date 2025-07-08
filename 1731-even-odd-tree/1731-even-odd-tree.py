# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque()
        q.append((root,0))
        while q:
            node = q.popleft()
            if node[0].left:
                q.append((node[0].left,node[1]+1))
            if node[0].right:
                q.append((node[0].right,node[1]+1))
            if node[1] % 2 == node[0].val % 2:
                return False
            if not q:
                break
            
            prv = q[0]
            if node[1] % 2 == 0:
                if prv[0].val <= node[0].val and prv[1] == node[1]:
                    return False
            else:
                if prv[0].val >= node[0].val and prv[1] == node[1]:
                    return False
        return True