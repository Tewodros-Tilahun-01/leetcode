class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            str_num = "".join( sorted(str(-num),reverse = True) )
            return -int(str_num)
        else:
            str_list = sorted(str(num))
            for i in range(len(str_list)):
                if str_list[i] != "0":
                    str_list[i] , str_list[0] = str_list[0] , str_list[i]
                    break
            return int("".join(str_list))
        
