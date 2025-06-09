class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        res = []
        for i in strs:
            if  tuple(sorted(i)) in count:
                count[  tuple(sorted(i)) ].append(i)
            else:
                count[  tuple(sorted(i))  ] = [i]
        for i in count:
            res.append(count[i])
        return res