class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []
        for i in s:
            if i != "#" :
                list1.append(i)
            elif len(list1) > 0:
                list1.pop()

        for i in t:
            if i != "#" :
                list2.append(i)
            elif len(list2) > 0:
                list2.pop()   
        return list1 == list2