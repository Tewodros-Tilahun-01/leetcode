class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            right = -1-i
            temp = s[i]
            s[i] = s[right]
            s[right] = temp
