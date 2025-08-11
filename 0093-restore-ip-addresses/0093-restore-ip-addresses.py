class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        res = []
        n = len(s)

        def backtrack(start: int, path: list[str]):
            print(path)
            # If we've formed 4 segments and used all chars
            if len(path) == 4:
                if start == n:
                    res.append(".".join(path))
                return

            # Try segments of length 1 to 3
            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start+length]
                
                # Skip invalid segments
                if (segment[0] == "0" and length > 1) or int(segment) > 255:
                    continue
                
                path.append(segment)
                backtrack(start + length, path)
                path.pop()

        backtrack(0, [])
        return res
