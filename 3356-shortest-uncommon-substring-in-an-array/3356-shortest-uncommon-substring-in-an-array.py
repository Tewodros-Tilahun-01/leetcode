class TrieNode:
    def __init__(self):
        self.children = {} 
        self.indices = set()  

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, substr: str, index: int):
        node = self.root
        for char in substr:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.indices.add(index)  
    
    def get_indices(self, substr: str) -> set:
        node = self.root
        for char in substr:
            if char not in node.children:
                return set()  
            node = node.children[char]
        return node.indices

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        trie = Trie()

        n = len(arr)
        for i in range(n):
            string = arr[i]
            m = len(string)
            for length in range(1,m+1):
                for start in range(m-length+1):
                    substr = string[start:start+length]
                    trie.insert(substr,i)

        res = [""] * n
        for i in range(n):
            string = arr[i]
            m = len(string)
            
            for length in range(1,m+1):
                substrings = []
                for start in range(m-length+1):
                    substr = string[start:start+length]
                    substrings.append(substr)

                substrings.sort()
                for sub in substrings:
                    if len(trie.get_indices(sub)) < 2:
                        res[i] = sub
                        break
                if res[i]:
                    break
        
        return res


                
            
            






            
        
