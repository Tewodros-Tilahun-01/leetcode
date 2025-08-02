class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hashmap = collections.defaultdict(int)
        count = 0
        for i in chars:
            hashmap[i] += 1
        for word in words:
            temp_map = hashmap.copy()
            valid = True
            
            for ch in word:
                if temp_map[ch] > 0:
                    temp_map[ch] -= 1
                else:
                    valid = False
                    break
            
            if valid:
                count += len(word)
        
        return count
