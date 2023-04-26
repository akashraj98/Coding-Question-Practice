class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        if s_nums[0]== s_nums[len(nums)//2]:
            return s_nums[0]
        elif s_nums[-1] == s_nums[len(nums)//2]:
            return s_nums[-1]
        else:
            return s_nums[len(nums)//2]