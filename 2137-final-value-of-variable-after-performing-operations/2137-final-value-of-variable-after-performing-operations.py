class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        op = {
        "--X":-1,
        "X++":1,
        "X--":-1,
        "++X":1}
        for i in operations:
            x += op[i]
        return x