class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_num = 2000
        dic1 = {}
        dic2 = {}
        res = []
        for i in range(len(list1)):
            st1 = list1[i]
            dic1[st1] = i
        for i in range(len(list2)):
            st1 = list2[i]
            if st1 in dic1:
                if min_num > i + dic1[st1]:
                    min_num = i + dic1[st1]
                    res = []
                    res.append(st1)
                elif min_num == i + dic1[st1]:
                    res.append(st1)
        return res
