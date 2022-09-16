class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        
        prefix, sufix, currmax = 0,0,float("-inf")
        for i in range(len(nums)):
            prefix = (prefix or 1)* nums[i]
            sufix  = (sufix or 1)* nums[-(i+1)]
            currmax = max(sufix,prefix,currmax)
        return currmax
        