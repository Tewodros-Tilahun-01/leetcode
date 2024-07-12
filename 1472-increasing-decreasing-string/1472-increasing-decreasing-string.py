class Solution:
    def sortString(self, s: str) -> str:
        my_list = sorted(list(s))
        result =""

        while(my_list):
            prv = ""
            for i in my_list[:]:
                if(prv<i):
                    result+=i
                    my_list.remove(i)
                    prv = i
            prv = ""
           
            for i in range(len(my_list)-1,-1,-1):
                if prv == "":
                    result+=my_list[i]
                    prv = my_list[i] 
                    my_list.pop(i)
                    continue 
                if(prv>my_list[i]):
                    result+=my_list[i]
                    prv = my_list[i] 
                    my_list.pop(i)
        return result