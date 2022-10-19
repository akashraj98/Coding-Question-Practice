import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hmap = Counter(words)
        heap = []
        for key,val in hmap.items():
            heapq.heappush(heap,(-val,key))
        res = []
        for i in range(k):
            freq,word = heapq.heappop(heap)
            res.append(word)
        return res
        