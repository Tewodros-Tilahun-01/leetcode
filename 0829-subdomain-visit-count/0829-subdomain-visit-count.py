class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        for p in cpdomains:
            n, d = p.split()
            n = int(n)
            s = d.split('.')
            for i in range(len(s)):
                t = '.'.join(s[i:])
                count[t] = count.get(t, 0) + n
        return [f"{v} {k}" for k, v in count.items()]
