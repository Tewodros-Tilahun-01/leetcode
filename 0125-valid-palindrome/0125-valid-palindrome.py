class Solution:
    def isPalindrome(self, s: str) -> bool:
        left ,right = 0, len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[right].lower() != s[left].lower():
                return False
            right -= 1
            left += 1
        return True
            