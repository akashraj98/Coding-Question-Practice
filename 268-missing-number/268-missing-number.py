class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums) 
        sn = n*(n+1)/2    # sum of n positive integers
        sum_nums=sum(nums)

        return int(sn -sum_nums)