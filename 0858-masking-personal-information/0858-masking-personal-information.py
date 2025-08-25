class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            s = s.lower()
            email = s.split("@")
            return email[0][0] + "*****" + email[0][-1] + "@" + email[1]
        else:
            digits = ''.join(c for c in s if c.isdigit()) 
            n = len(digits)
            local_number = digits[-4:]  
            if n == 10:  
                return f"***-***-{local_number}"
            elif n == 11:  
                return f"+*-***-***-{local_number}"
            elif n == 12: 
                return f"+**-***-***-{local_number}"
            else:  
                return f"+***-***-***-{local_number}"