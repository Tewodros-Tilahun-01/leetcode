class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = [] 
        def backtrack(ip,i):
            if i == len(s) and len(ip) == 4:
                res.append(  ".".join( map(str,ip) ) ) 
                return 
            if len(ip) > 3:
                return 

            for j in range(i,len(s)):
                st = "".join(s[i:j+1]) 
                val = int(st)
                if val <= 255 and len(st) == len(str(val)):
                    ip.append(val)
                    backtrack(ip,j+1)
                    val = ip.pop()
                
                
                
        ip = []
        backtrack(ip,0)
        return res
