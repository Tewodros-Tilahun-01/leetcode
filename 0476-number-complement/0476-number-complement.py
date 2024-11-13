class Solution:
    def findComplement(self, num: int) -> int:
        binary_string = format(num, 'b')
        res = []
        for i in binary_string:
            if i=="0":
                res.append("1") 
            else: res.append("0")
        decimal = int("".join(res),2)
        return decimal