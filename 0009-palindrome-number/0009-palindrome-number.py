class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0):
            return False
        string = str(x)
        palidrome = True
        mid = len(string)//2
        x = 0
        for i in range(mid):
            if(string[x] != string[-1-x]):
                palidrome =  False
            x = x + 1
        return palidrome