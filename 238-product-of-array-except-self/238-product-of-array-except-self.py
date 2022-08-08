class Solution:
    def productExceptSelf(self, A: List[int]) -> List[int]:
        
        c_zero = 0
        mul = 1
        indx_zero = 0
        res = []
        for index,val in enumerate(A):
            if val == 0:
                c_zero+=1
                indx_zero = index  
                continue
            mul = mul*val

        if c_zero > 1:
            return [0]*len(A)
        if c_zero ==1:
            ans = [0]*len(A)
            ans[indx_zero] = mul
            return ans

        for i in A:
            if i == 0:
                res.append(mul)
            res.append(mul//i)
        return res
        # p = 1
        # out = []
        # for i in range(len(nums)):
        #     out.append(p)
        #     p = p* nums[i]
        # p=1
        # for j in range(len(out)-1,-1,-1):
        #     out[j] = p* out[j]
        #     p = p* nums[j]
        # return out