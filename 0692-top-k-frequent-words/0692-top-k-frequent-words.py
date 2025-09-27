class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frq = Counter(words)
        
        heap = []
        for key , value in frq.items():
            heapq.heappush(heap,(-value,key))
        
        res = []
        for i in range(k):
            word = heapq.heappop(heap)[1]
            res.append(word)

        return res
        