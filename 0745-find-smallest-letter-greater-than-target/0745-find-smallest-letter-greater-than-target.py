class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        next_to_target = ord(target) + 1
        for i in range(next_to_target, ord("z")+1):
            if chr(i) in letters:
                return chr(i)
        return letters[0]