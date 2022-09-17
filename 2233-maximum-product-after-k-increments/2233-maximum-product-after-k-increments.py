
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        for i in range(k):
            heappush(nums,heappop(nums)+1)
        # r = 1
        # for num in nums: r = (r*num)%(10**9+7)
        # return r
        return reduce(lambda acc,n : (acc*n)%(10**9+7),nums)
        
            
        