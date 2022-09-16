class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Modified kadane algorithm
        # at each iteration we check max and min prod using suffix and prefix arr
        # we take max of suffix, prefix, currtmax and update our max
        # in case of zero we have to handle it by taking 1 insted 0 pref or suf
        
        prefix, sufix, currmax = 0,0,float("-inf")
        for i in range(len(nums)):
            prefix = (prefix or 1)* nums[i]
            sufix  = (sufix or 1)* nums[-(i+1)]
            currmax = max(sufix,prefix,currmax)
        return currmax
        