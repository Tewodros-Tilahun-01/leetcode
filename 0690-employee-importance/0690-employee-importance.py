"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int: 
        
        def dfs(id):
            total = 0
            for node in hashmap[id].subordinates:
                total += dfs(node)
            return total + hashmap[id].importance

        hashmap = {}
        for i in employees:
               hashmap[i.id] = i
        return dfs(id)
               