# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = collections.defaultdict(list)
        q = collections.deque()
        res = []

        def change_to_graph(graph,node):
            if not node:
                return
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            change_to_graph(graph,node.left)
            change_to_graph(graph,node.right)
        change_to_graph(graph,root)

        q.append((target.val,0))
        visited = set()
        while q:
            val , step = q.popleft()  
            visited.add(val)  
            for nb in graph[val]:
                if nb not in visited and step < k:
                    q.append((nb,step+1))
            if step == k:
                res.append(val)
        return res
        
