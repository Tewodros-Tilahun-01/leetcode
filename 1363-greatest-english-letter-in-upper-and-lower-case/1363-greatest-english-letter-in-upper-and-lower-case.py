class Solution:
    def greatestLetter(self, s: str) -> str:
        count = set()
        maxnum = 0
        for i in s:
            if i.swapcase() in count:
                maxnum = max (maxnum , ord(i.lower()) )
            else:
                count.add(i)
        return  "" if not maxnum else chr(maxnum).upper()