class Solution:
    def eventualSafeNodes(self,adj_list):
        size = len(adj_list)
        status = [0] * size
        
        def explore(vertex):
            if status[vertex] == 1:
                status[vertex] = 3
                return False
            if status[vertex] == 2:
                return True
            if status[vertex] == 3:
                return False
            
            status[vertex] = 1
            
            for next_vertex in adj_list[vertex]:
                if not explore(next_vertex):
                    status[vertex] = 3
                    return False
            
            status[vertex] = 2
            return True
        
        for vertex in range(size):
            if status[vertex] == 0:
                explore(vertex)
        
        result = [vertex for vertex in range(size) if status[vertex] == 2]
        return sorted(result)