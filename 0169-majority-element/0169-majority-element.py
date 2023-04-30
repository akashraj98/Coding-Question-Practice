class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        return s_nums[len(nums)//2]