class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
#         count = 0
#         start = 0
#         end = 1
#         n = len(nums)
#         sm = nums[start]
#         while start< n:
#             while end< n and sm < k:
#                 sm+=nums[end]
#                 end+=1
#                 if sm == k:
#                     count+=1
                
#             sm-=nums[start]
#             start+=1

#         return count
                
        
                    
                
        res = 0
        sm = 0
        pre_map = {0:1}
        for num in nums:
            sm+=num
            if sm-k in pre_map:
                res+=pre_map[sm-k]
            pre_map[sm] = pre_map.get(sm,0)+1
        return res