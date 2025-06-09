class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for i in strs:
            if  tuple(sorted(i)) in count:
                count[  tuple(sorted(i)) ].append(i)
            else:
                count[  tuple(sorted(i))  ] = [i]
        return list(count.values())