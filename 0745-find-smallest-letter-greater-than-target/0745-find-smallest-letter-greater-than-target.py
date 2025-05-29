class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        smallest = letters[0]
        for i in letters:
            if i > target:
                 return i
        return smallest