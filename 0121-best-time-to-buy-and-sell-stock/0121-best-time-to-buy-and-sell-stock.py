class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        min_no = nums[0] # min so far
        profit = 0
        for i in range(len(nums)):
            if nums[i]<min_no:
                min_no = min(min_no,nums[i])
            profit = max(profit,nums[i]-min_no)
        return profit