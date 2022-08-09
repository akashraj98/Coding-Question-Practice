class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
#         c_zero = 0
#         mul = 1
#         indx_zero = 0
#         res = []
#         for index,val in enumerate(A):
#             if val == 0:
#                 c_zero+=1
#                 indx_zero = index  
#                 continue
#             mul = mul*val

#         if c_zero > 1:
#             return [0]*len(A)
#         if c_zero ==1:
#             ans = [0]*len(A)
#             ans[indx_zero] = mul
#             return ans

#         for i in A:
#             if i == 0:
#                 res.append(mul)
#             res.append(mul//i)
#         return res
        prefix = 1  # first prefix will always be 1
        res = []
        for i in range(len(nums)):
            res.append(prefix)
            prefix = prefix* nums[i]
        postfix =1  # fist post fix from last will always be 1
        
        for j in range(len(res)-1,-1,-1):
            res[j]= res[j]* postfix
            postfix = postfix* nums[j]
        return res