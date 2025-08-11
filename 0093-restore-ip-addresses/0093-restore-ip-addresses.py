class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        
        def backtrack(start: int, parts: List[int], count: int):
            # Base case: valid IP address found
            if count == 4 and start == n:
                res.append(".".join(map(str, parts)))
                return
            
            # Early termination: too many parts or not enough digits
            if count > 4 or start >= n or (4 - count) * 3 < n - start:
                return
                
            # Try segments of length 1 to 3
            for length in range(1, min(4, n - start + 1)):
                segment = s[start:start + length]
                
                # Skip if segment starts with '0' and has multiple digits
                if len(segment) > 1 and segment[0] == '0':
                    continue
                    
                # Convert to integer and validate
                val = int(segment)
                if val > 255:
                    continue
                    
                # Recurse with this segment
                parts.append(val)
                backtrack(start + length, parts, count + 1)
                parts.pop()

        backtrack(0, [], 0)
        return res