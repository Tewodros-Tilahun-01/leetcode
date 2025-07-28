class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        def dfs(index,fair):
            if index == len(cookies):
                fair = min( fair , max(child) )
                return fair
            for i in range(k):
                child[i] += cookies[index]
                fair = min(dfs(index+1,fair) , fair)
                child[i] -= cookies[index]
                if child[0] == 0:
                    break
            return fair

        child = [0] * k
        return dfs(0,float("inf"))




        

            
        
