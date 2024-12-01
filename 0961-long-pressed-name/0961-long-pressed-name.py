class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        pt1 , pt2 =  0 , 0
        while pt1 < len(name) and pt2 < len(typed):
            if name[pt1] != typed[pt2]:
                return False
            count1 , count2  =  0 , 0
            while pt1 < len(name)-1 and name[pt1] == name[pt1 + 1]:
                count1 += 1
                pt1 += 1
            while pt2 < len(typed)-1 and typed[pt2] == typed[pt2 +1] :
                count2 += 1
                pt2 += 1
            if count1 > count2:
                return False
            pt1 += 1
            pt2 += 1
        if pt2 != len(typed) or pt1 != len(name):
            return False
        return True