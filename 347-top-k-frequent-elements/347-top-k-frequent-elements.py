class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        li =[]
        res = []
        for key,value in count.items():
            li.append([value,key])
        li.sort(reverse=True)
        for i in range(k):
            res.append(li[i][-1])
        return res
            
            
        
            