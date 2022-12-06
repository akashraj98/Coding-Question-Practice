class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i >= last_pos:
                last_pos =i
        return last_pos ==0
        
#         res = False
#         end_indx = len(nums)-1
#         # memo = {}
#         def f(pos) -> bool:
#             if pos == len(nums)-1: 
#                 # memo[pos]= True
#                 return True
#             if nums[pos] ==0 and pos < end_indx:
#                 # memo[pos] = False
#                 return False
#             if pos > end_indx: 
#                 memo[pos] = True
#                 return False
            
#             for i in range(1,nums[pos]+1):
#                 nonlocal res
#                 # if pos+i in memo:
#                 #     res = res or memo[pos+i]
#                 # else:
#                 res = res or f(pos+i)
#             return res
#         return f(0)